from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event,Venue
from .forms import VenueForm

def show_venue(request,venue_id):
	venue = Venue.objects.get(pk=venue_id)
	return render(request, 'EventsApp/show_venue.html',{
		'venue':venue,
		})


def list_venues(request):
	venue_list = Venue.objects.all()
	return render(request, 'EventsApp/venue.html',{
		'venue_list':venue_list,
		})
def add_venue(request):
	submitted = False
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_venue?submitted=True')
	else:
		form = VenueForm
		if 'submitted' in request.GET:
			submitted = True
	form = VenueForm
	return render(request, 'EventsApp/add_venue.html',{'form' : form, 'submitted':submitted})

def all_events(request):
	event_list = Event.objects.all()
	return render(request, 'EventsApp/event_list.html',{
		'event_list':event_list,
		})

def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
	name = 'Don'
	month = month.capitalize()
	#Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	#Create a calendar
	cal = HTMLCalendar().formatmonth(
		year,
		month_number)

	#get current year/time
	now = datetime.now()
	current_year = now.year

	#get current time
	time = now.strftime('%I:%M %p')
	return render(request, 'EventsApp/home.html',{
		"name" : name,
		"year" : year,
		"month": month,
		"month_number" : month_number,
		"cal": cal,
		"current_year": current_year,
		"time": time
		})

# Create your views here.
