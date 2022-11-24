from django.shortcuts import render
from datetime import datetime
from .models import *

# Create your views here.
def HomeView(request):
    return render(request, 'main/home.html')

def TrainMaintenance(request):

    trains = Train.objects.all()
    maintenance_crew = MaintenanceCrew.objects.all()
    crew_certificates = CrewCertificate.objects.all()
    maintenance_certficates = {}

    context = {
        'trains' : trains,
        'maintenance_crew' : maintenance_crew,
    }

    return render(request, 'main/train_maintenance.html', context)
    
def TrainDetail(request, pk):

    train = Train.objects.get(train_id=pk)

    maint_cert = MaintenanceCertificate.objects.filter(train_id=train)
    if len(maint_cert) > 0:
        maint_cert = MaintenanceCertificate.objects.filter(train_id=train)[0]
        crew_certs = CrewCertificate.objects.filter(certificate_no=maint_cert).order_by('maintenance_date')
    else:
        crew_certs = None

    context = {
        'train' : train,
        'crew_certs' : crew_certs,
    }

    return render(request, 'main/train_detail.html', context)

def TrainRoutes(request):

    local_stations = LocalStation.objects.all()
    town_stations = TownStation.objects.all()
    inter_town_routes = InterTownRoute.objects.all().order_by('origin')

    local = {}
    inter = {}
    town = {}

    for l in local_stations:
        origin = Station.objects.get(station_id=l.station_id)
        destination = Station.objects.get(station_id=l.destination.station_id)
        local[origin] = destination

    for t in town_stations:
        station = Station.objects.get(station_id=t.station_id)
        town[t] = station

    for i in inter_town_routes:
        origin = Station.objects.get(station_id=i.origin.station_id)
        destination = Station.objects.get(station_id=i.destination.station_id)
        
        inter[i] = [origin, destination, i.travel_time, f'{i.trip_cost} Lion coins']

    context = {
        'local' : local,
        'inter' : inter, 
        'town' : town,
    }

    return render(request, 'main/train_routes.html', context)

def DepartureRoutes(request, pk):

    town = TownStation.objects.get(station_id=pk)
    town_routes = InterTownRoute.objects.filter(origin=town)

    routes = {}

    for tr in town_routes:
        origin = Station.objects.get(station_id=town.station_id)
        destination = Station.objects.get(station_id=tr.destination.station_id)
        duration = tr.travel_time
        cost = f'{tr.trip_cost} Lion coins'
        routes[tr.route_id] = [origin, destination, duration, cost]

    context = {
        'routes' : routes,
    }



    return render(request, 'main/depart.html', context) 

def ArrivalRoutes(request, pk):

    town = TownStation.objects.get(station_id=pk)
    town_routes = InterTownRoute.objects.filter(destination=town)

    routes = {}

    for tr in town_routes:
        origin = Station.objects.get(station_id=tr.origin.station_id)
        destination = Station.objects.get(station_id=town.station_id)
        duration = tr.travel_time
        cost = f'{tr.trip_cost} Lion coins'
        routes[tr.route_id] = [origin, destination, duration, cost]

    context = {
        'routes' : routes,
    }

    return render(request, 'main/arrive.html', context) 

def TripSchedules(request):

    trips = TripDate.objects.all()

    context = {
        'trips' : trips,
    }
    return render(request, 'main/trip_schedules.html', context)

def TicketSales(request):
    return render(request, 'main/home.html')