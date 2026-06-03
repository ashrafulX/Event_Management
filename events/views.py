from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import CategoryModelForm,ParticipantModelForm,EventModelForm
from django.contrib import messages
from events.models import Event, Category, Participant
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Count
from .models import Event, Participant
from django.db.models import Count, Q
from django.utils import timezone
def dashboard(request):

    today=timezone.now().date()


    """STATS ER MODDE COUNT  BER KORTE HOBE"""

    stats=Event.objects.aggregate(
        total_events=Count('id'),
        upcoming=Count('id',filter=Q(date__gt=timezone.now())),
        past=Count('id',filter=Q(date__lt=timezone.now()))
    )

    participant_stats = Participant.objects.aggregate(total_participants_count=Count('id'))
    total_participants = participant_stats['total_participants_count']
    
    allevent = Event.objects.order_by('date')
    
    if stats['total_events'] > 3:
        event = allevent[:3]
    else:
        event = allevent
        
    context = {
        'events': event,
        'total_participants': total_participants,
        'total_events': stats['total_events'],
        'upcoming':stats['upcoming'],
        'past':stats['past']
    }
    
    return render(request, 'dashboard.html', context)


def create_category(request):
    if request.method=='POST':
        form=CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Created Succesfully')
            return redirect('create-category')
    else:
        form=CategoryModelForm()
        
    context={'formss':form}
    return render(request,'category.html',context)


def create_participant(request):
    person=ParticipantModelForm()
    if request.method=='POST':
        person=ParticipantModelForm(request.POST)
        if person.is_valid():
            person.save()
            messages.success(request,'Paricipant Added Succesfully')
            return redirect('create-participant')
    context={'person':person}
    return render(request,'participant.html',context)


def create_event(request):
    event=EventModelForm()
    if request.method=='POST':
        event=EventModelForm(request.POST)
        if event.is_valid():
            event.save()
            messages.success(request,'Event Created Succesfully')
            return redirect('create-event')
        else:
            print(event.errors)
    context={'event':event}
    return render(request,'create_event.html',context)


def update(request,id):
    pass
#     obj=Event.objects.get(id=id)
