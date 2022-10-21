from django.contrib import admin

# Register your models here.
from .models import Airport, Flight, Passenger

admin.site.register(Airport)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("duration", "__str__")

admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)
