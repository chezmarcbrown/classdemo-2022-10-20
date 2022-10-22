from django.contrib import admin

# Register your models here.
from .models import Airport, Flight, Passenger, Booking

admin.site.register(Airport)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("duration", "__str__")
admin.site.register(Flight, FlightAdmin)

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
admin.site.register(Passenger, PassengerAdmin) 

admin.site.register(Booking)
