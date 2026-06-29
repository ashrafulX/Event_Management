from django.shortcuts import render,redirect
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

def allevent(request):
    events=Event.objects.order_by('date')
    return render(request,'allevent.html',{'events':events})



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
    obj=Event.objects.get(id=id)
    event=EventModelForm(instance=obj)

    if request.method=='POST':
        event=EventModelForm(request.POST,instance=obj)
        if event.is_valid():
            event.save()
            messages.success(request,'Event Update Succesfully')
            return redirect('create-event')
        else:
            print(event.errors)
    context={'event':event}
    return render(request,'create_event.html',context)


def delete(request,id):
    if request.method=="POST":
        obj=Event.objects.get(id=id)
        obj.delete()
        messages.success(request, "Event deleted successfully!")
    return redirect("all-event")


def upcoming(request):
    today=timezone.now().date()
    stats = Event.objects.aggregate(
        total_events=Count('id'),
        upcoming=Count('id', filter=Q(date__gt=today)),
        past=Count('id', filter=Q(date__lt=today))
    )
    participant_stats = Participant.objects.aggregate(total_participants_count=Count('id'))
    total_participants = participant_stats['total_participants_count']
    
    upcoming_events = Event.objects.filter(date__gt=today).order_by('date')
    
    context = {
        'events': upcoming_events,
        'total_participants': total_participants,
        'total_events': stats['total_events'],
        'upcoming': stats['upcoming'],
        'past': stats['past']
    }
    return render(request, 'upcoming.html', context)


def past(request):
    past=Event.objects.aggregate(past=Count('id',filter=Q(date__lt=timezone.now().date())))['past']
    past_events = Event.objects.filter(date__lt=timezone.now().date()).order_by('date')
    context={
        'events':past_events,
        'past':past,
    }
    return render(request,'past.html',context)


def search(request):
    query=request.GET.get('q')
    result=Event.objects.all()

    if query:
        result=Event.objects.filter(Q(name__icontains=query) | Q(location__icontains=query) | Q(category__name__icontains=query)).distinct()
    
    context={
        'events':result,
        'query':query
    }
    return render(request,'search.html',context)