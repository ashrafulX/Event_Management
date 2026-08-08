from django  import forms
import re
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from events.forms import styleMixin
from django.contrib.auth.models import User
class RegisterForm(styleMixin,UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_exist=User.objects.filter(email=email).exists()

        if email_exist:
            raise forms.ValidationError('Email Already Exist')
        
        return email
    
    def clean_password1(self):
        password=self.cleaned_data.get('password1')
        errors=[]
        if len(password) < 8:
            errors.append('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password):
            errors.append('Password must include at least one uppercase letter.')
        if not re.search(r'[a-z]', password):
            errors.append('Password must include at least one lowercase letter.')
        if not re.search(r'[0-9]', password):
            errors.append('Password must include at least one number.')
        if not re.search(r'[@#$%^&+=]', password):
            errors.append('Password must include at least one special character.')

        if errors:
            raise forms.ValidationError(errors)
        return password
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password1')
        confirm_password=cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password Did not Same. Both Password Must be Same')
        return cleaned_data


class login_form(styleMixin,AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 text-slate-900 placeholder-slate-400 focus:bg-white focus:outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 transition-all duration-200",
            "placeholder": "Enter your username",
        })

        self.fields["password"].widget.attrs.update({
            "class": "w-full px-4 py-3 rounded-lg border border-slate-300 bg-slate-50 text-slate-900 placeholder-slate-400 focus:bg-white focus:outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 transition-all duration-200",
            "placeholder": "Enter your password",})


class Changepassword(styleMixin,PasswordChangeForm):
    pass

class PasswordResetForm(styleMixin,PasswordResetForm):
    pass

class PasswordResetConfirmForm(styleMixin,SetPasswordForm):
    pass


class EditProfileModelForm(styleMixin,forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

    bio=forms.CharField(required=False,widget=forms.Textarea,label='bio')
    profile=forms.ImageField(required=False,label='Profile Picture')


    def __init__(self,*args,**kwargs):
        self.userprofile = kwargs.pop('userprofile', None)
        super().__init__(*args,**kwargs)

        #error handle

        if self.userprofile:
            self.fields['bio'].initial=self.userprofile.bio
            self.fields['profile'].initial=self.userprofile.profile

    def save(self,commit=True):
        user=super().save(commit=False)

        if self.userprofile:
                new_profile = self.cleaned_data.get('profile')
                old_profile = self.userprofile.profile

        if new_profile:
            self.userprofile.profile = new_profile
            self.userprofile.save()

            if old_profile:
                old_profile.delete(save=False)

            if commit:
                self.userprofile.save()

        if new_profile and old_profile:

            if old_profile.name != self.userprofile.profile.name:
                old_profile.delete(save=False)

                if commit:
                    user.save()

        return user