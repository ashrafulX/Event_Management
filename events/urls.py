# from django.contrib import admin
from django.urls import path,include
from events.views import create_category,create_participant,create_event,update,upcoming,past,delete,allevent,search,CreateEvent,Allevent,Upcoming

urlpatterns = [
    path('create_category/',create_category,name='create-category'),
    path('create_participant/',create_participant,name='create-participant'),
    # path('create_event/',create_event,name='create-event'),
    path('create_event/',CreateEvent.as_view(),name='create-event'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    # path('upcoming/',upcoming,name='upcoming-events'),
    path('upcoming/',Upcoming.as_view(),name='upcoming-events'),
    path('past/',past,name='past-events'),
    # path('all-event/',allevent,name='all-event'),
    path('all-event/',Allevent.as_view(),name='all-event'),
    path('search/', search, name='search'),
    

]