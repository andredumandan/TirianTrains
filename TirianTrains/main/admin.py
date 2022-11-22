from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Train)
admin.site.register(MaintenanceCrew)
admin.site.register(MaintenanceCertificate)
admin.site.register(CrewCertificate)
admin.site.register(Task)
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Station)
admin.site.register(LocalStation)
admin.site.register(TownStation)
admin.site.register(InterTownRoute)
admin.site.register(Trip)
admin.site.register(LocalTrip)
admin.site.register(InterTownTrip)
admin.site.register(TicketTrip)