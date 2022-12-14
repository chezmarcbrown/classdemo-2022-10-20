import re
from django.shortcuts import render, redirect
from .models import Flight, Passenger, Booking

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

from django.http import Http404

def flight(request, flight_id):
    try:
        f = Flight.objects.get(id = flight_id)
    except Flight.DoesNotExist:
        raise Http404("flight not found")
    return render(request, "flights/flight.html", {
        "flight": f,
        "non_passengers": Passenger.objects.exclude(flights=f).all(),
        "passengers": f.passengers.all(),
        "bookings": Booking.objects.filter(flight=f)
    })

def book(request, flight_id):
    if request.method == "POST":
        p = Passenger.objects.get(pk=request.POST["passenger"])
        flight = Flight.objects.get(pk=flight_id)
        b = Booking(passenger=p, flight=flight, booker=request.user)
        b.save()
        #p.flights.add(flight)
        return redirect("flights:flight", flight_id=flight_id)
