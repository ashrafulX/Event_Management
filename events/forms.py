from django import forms
# from django.forms import ModelForm
from events.models import Category,Participant, Event

class styleMixin:
    default_design = "w-full mt-2 mx-2 my-2 border-2 border-gray-100 rounded-lg focus:border-red-600"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styles()

    def apply_styles(self):
        for field_name, field in self.fields.items():
            label_text = field.label or field_name.replace('_', ' ')
            placeholder_text = f"Enter {label_text.lower()}"

            existing_classes = field.widget.attrs.get('class', '')
            new_classes = f"{existing_classes} {self.default_design}".strip()

            field.widget.attrs.update({
                'class': new_classes,
                'placeholder': placeholder_text
            })


class CategoryModelForm(styleMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']



class ParticipantModelForm(styleMixin,forms.ModelForm):
    
    class Meta:
        model=Participant
        fields=['name','email']


class EventModelForm(styleMixin,forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','description','date','time','location','category','participants','ticket']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'participants': forms.CheckboxSelectMultiple(),
            }
        