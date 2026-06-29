from django.contrib import admin

# Register your models here.
from .models import Category, Participant, Event
admin.site.register(Category)
admin.site.register(Participant)
admin.site.register(Event)