# from django.contrib import admin
from django.urls import path,include
from events.views import create_category,create_participant,create_event,update,upcoming,past

urlpatterns = [
    path('create_category/',create_category,name='create-category'),
    path('create_participant/',create_participant,name='create-participant'),
    path('create_event/',create_event,name='create-event'),
    path('create_event/',create_event,name='create-event'),
    path('update/<int:id>/',update,name='update'),
    path('upcoming/',upcoming,name='upcoming-events'),
    path('past/',past,name='past-events')
    

]