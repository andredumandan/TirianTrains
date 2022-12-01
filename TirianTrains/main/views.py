from django.shortcuts import render, redirect
from .models import *
from datetime import datetime, timedelta

# Create your views here.
def HomeView(request):

    if request.method == 'POST':
        form = request.POST
        date = form.get('date') 
        return redirect('reports', date)

    date_today = datetime.now().date()
    # https://stackoverflow.com/questions/441147/how-to-subtract-a-day-from-a-date
    date_week  = [date_today - timedelta(days=7), date_today]

    tickets_today = Ticket.objects.filter(date_purchased=date_today)
    tickets_week = Ticket.objects.filter(date_purchased__range=date_week)
    tickets_month = Ticket.objects.filter(
        date_purchased__year=date_today.year,
        date_purchased__month=date_today.month
    )
    tickets_year = Ticket.objects.filter(
        date_purchased__year=date_today.year
    )
    tickets_all = Ticket.objects.all()

    today_total = 0
    for ticket in tickets_today:
        for ticket_trip in ticket.tickettrip_set.all():
            if ticket_trip.trip.type == 'local':
                today_total += 2
            elif ticket_trip.trip.type == 'inter-town':
                today_total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost

    week_total = 0
    for ticket in tickets_week:
        for ticket_trip in ticket.tickettrip_set.all():
            if ticket_trip.trip.type == 'local':
                week_total += 2
            elif ticket_trip.trip.type == 'inter-town':
                week_total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost

    month_total = 0
    for ticket in tickets_month:
        for ticket_trip in ticket.tickettrip_set.all():
            if ticket_trip.trip.type == 'local':
                month_total += 2
            elif ticket_trip.trip.type == 'inter-town':
                month_total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost

    year_total = 0
    for ticket in tickets_year:
        for ticket_trip in ticket.tickettrip_set.all():
            if ticket_trip.trip.type == 'local':
                year_total += 2
            elif ticket_trip.trip.type == 'inter-town':
                year_total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost

    all_time_total = 0
    for ticket in tickets_all:
            for ticket_trip in ticket.tickettrip_set.all():
                if ticket_trip.trip.type == 'local':
                    all_time_total += 2
                elif ticket_trip.trip.type == 'inter-town':
                    all_time_total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost

    sales = {}
    sales['This Day'] = [date_today, today_total]
    sales['Past 7 Days'] = [f"{date_week[0].strftime('%b. %d, %Y')} - {date_today.strftime('%b. %d, %Y')}", week_total]
    sales['Past Month'] = [f"{date_today.strftime('%b. %Y')}", month_total]
    sales['Past Year'] = [f"{date_today.strftime('%Y')}", year_total]

    context = {
        'sales' : sales,
        'total' : all_time_total,
    }

    return render(request, 'main/home.html', context)

def Reports(request, date):

    
    tickets_today = Ticket.objects.filter(date_purchased=date)
    print(tickets_today)

    total = 0
    for ticket in tickets_today:
        for ticket_trip in ticket.tickettrip_set.all():
            if ticket_trip.trip.type == 'local':
                total += 2
            elif ticket_trip.trip.type == 'inter-town':
                total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost

    tickets = {}

    for ticket in tickets_today:
        ticket_total = 0
        for ticket_trip in ticket.tickettrip_set.all():
            if ticket_trip.trip.type == 'local':
                ticket_total += 2
            elif ticket_trip.trip.type == 'inter-town':
                ticket_total += InterTownTrip.objects.get(trip_id = ticket_trip.trip.trip_id).route.trip_cost
        tickets[ticket] = [ticket.customer,ticket_total]

    certificates = CrewCertificate.objects.filter(maintenance_date=date)

    crew_certs = {}

    for cert in certificates:
        crew_certs[cert] = [
            cert.certificate_no.train.train_id,
            cert.certificate_no.train,
            cert.crew_no,
            cert.task,
            cert.condition,
        ]

    context = {
        'date' : datetime.strptime(date, '%Y-%m-%d').strftime('%b. %m %Y'),
        'total' : total,
        'tickets' : tickets,
        'crew_certs' : crew_certs,
    }

    return render(request, 'main/reports.html', context)

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

    trip_dates = TripDate.objects.all()

    trips = {}

    for date in trip_dates:
        trips[date] = len(date.trip_set.all())

    context = {
        'trips' : trips,
    }
    return render(request, 'main/trip_schedules.html', context)

def TripDateDetail(request, pk):

    trip_date = TripDate.objects.get(date=pk)
    trip_objects = trip_date.trip_set.all()

    trips = {}
    local_trips = {}

    for trip in trip_objects:
        if trip.type == 'inter-town':
            route = InterTownTrip.objects.get(trip_id=trip.trip_id).route
            origin = Station.objects.get(station_id=route.origin.station_id)
            destination = Station.objects.get(station_id=route.destination.station_id)
            trips[trip] = [trip.train.train_id, origin, destination, trip.departure_time, trip.departure_time, route.travel_time, route.trip_cost]
        elif trip.type == 'local':
            route = LocalTrip.objects.get(trip_id=trip.trip_id).station
            origin = Station.objects.get(station_id=route.station_id)
            destination = Station.objects.get(station_id=route.destination.station_id)
            local_trips[trip] = [trip.train.train_id, origin, destination, trip.departure_time, trip.departure_time, 5, 2]

    context = {
        'trips' : trips,
        'local_trips' : local_trips,
        'date' : trip_date,
    }
    return render(request, 'main/schedule_detail.html', context)

def Trips(request):
    
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

    return render(request, 'main/trips.html', context)

def TripDetail(request, type, pk):
    
    trips = {}

    if type == 'local':
        origin = Station.objects.get(station_id=pk)
        local_trips = LocalTrip.objects.filter(station=LocalStation.objects.get(station_id=origin.station_id))

        for trip in local_trips:

            date = Trip.objects.get(trip_id=trip.trip_id).trip_date
            train = Trip.objects.get(trip_id=trip.trip_id).train
            destination = Station.objects.get(station_id=LocalStation.objects.get(station_id=origin.station_id).destination.station_id)
            departure = Trip.objects.get(trip_id=trip.trip_id).departure_time
            arrival = Trip.objects.get(trip_id=trip.trip_id).departure_time
            duration = 5
            cost = 2

            trips[trip] = [date.date, train.train_id, origin, destination, departure, arrival, duration, cost]
    
    elif type == 'inter-town-depart':
        s_origin = Station.objects.get(station_id=pk)
        origin = TownStation.objects.get(station_id=pk)
        routes = InterTownRoute.objects.filter(origin=origin)
        
        for route in routes:
            town_trips = InterTownTrip.objects.filter(route=route)
            for t_t in town_trips:
                trip = Trip.objects.get(trip_id=t_t.trip_id)
                date = trip.trip_date
                train = trip.train
                destination = Station.objects.get(station_id=route.destination.station_id)
                departure = trip.departure_time
                arrival = trip.departure_time
                duration = route.travel_time
                cost = route.trip_cost

                trips[trip] = [date.date, train.train_id, s_origin, destination, departure, arrival, duration, cost]

    elif type == 'inter-town-arrive':
        s_destination = Station.objects.get(station_id=pk)
        destination = TownStation.objects.get(station_id=pk)
        routes = InterTownRoute.objects.filter(destination=destination)
        
        for route in routes:
            town_trips = InterTownTrip.objects.filter(route=route)
            for t_t in town_trips:
                trip = Trip.objects.get(trip_id=t_t.trip_id)
                date = trip.trip_date
                train = trip.train
                origin = Station.objects.get(station_id=route.origin.station_id)
                departure = trip.departure_time
                arrival = trip.departure_time
                duration = route.travel_time
                cost = route.trip_cost

                trips[trip] = [date.date, train.train_id, origin, s_destination, departure, arrival, duration, cost]

    context = {
        'trips' : trips,
    }

    return render(request, 'main/trip_details.html', context)

def Tickets(request):

    ticket_objects = Ticket.objects.all()

    tickets = {}
    for ticket in ticket_objects:
        
        if len(ticket.tickettrip_set.all()) > 0:

            first_trip = ticket.tickettrip_set.first().trip
            last_trip = ticket.tickettrip_set.last().trip
            
            if first_trip.type == 'local':
                origin = Station.objects.get(station_id=LocalTrip.objects.get(trip_id=first_trip.trip_id).station.station_id)

            elif first_trip.type == 'inter-town':
                origin = Station.objects.get(station_id=InterTownTrip.objects.get(trip_id=first_trip.trip_id).route.origin.station_id)

            if last_trip.type == 'local':
                final_dest = Station.objects.get(station_id=LocalTrip.objects.get(trip_id=last_trip.trip_id).station.destination.station_id)

            elif last_trip.type == 'inter-town':
                final_dest = Station.objects.get(station_id=InterTownTrip.objects.get(trip_id=last_trip.trip_id).route.destination.station_id)

            total_cost = 0
            for ticket_trip in ticket.tickettrip_set.all():
                if ticket_trip.trip.type == 'local':
                    total_cost += 2
                elif ticket_trip.trip.type == 'inter-town':
                    trip_cost = InterTownTrip.objects.get(trip_id=ticket_trip.trip.trip_id).route.trip_cost
                    total_cost += trip_cost

            tickets[ticket] = [origin, final_dest, total_cost]

    context = {
        'tickets' : tickets,
    }
    return render(request, 'main/tickets.html', context)

def TicketDetail(request, pk):
    
    ticket = Ticket.objects.get(ticket_id=pk)
    customer_obj = ticket.customer
    
    ticket_trips = ticket.tickettrip_set.all()
    trips = {}
    customer = {}


    for t_t in ticket_trips:

        trip = t_t.trip
        train = trip.train.train_id

        if trip.type == 'local':
            origin = Station.objects.get(station_id=LocalTrip.objects.get(trip_id=trip.trip_id).station.station_id)
            destination = Station.objects.get(station_id=LocalTrip.objects.get(trip_id=trip.trip_id).station.destination.station_id)
            departure = trip.departure_time
            arrival = trip.departure_time
            duration = 5
            cost = 2

        elif trip.type == 'inter-town':
            origin = Station.objects.get(station_id=InterTownTrip.objects.get(trip_id=trip.trip_id).route.origin.station_id)
            destination = Station.objects.get(station_id=InterTownTrip.objects.get(trip_id=trip.trip_id).route.destination.station_id)
            departure = trip.departure_time
            arrival = trip.departure_time
            duration = InterTownTrip.objects.get(trip_id=trip.trip_id).route.travel_time
            cost = InterTownTrip.objects.get(trip_id=trip.trip_id).route.trip_cost

        trips[t_t] = [train, origin, destination, departure, arrival, duration, cost]

    total_cost = 0
    for ticket_trip in ticket_trips:
        if ticket_trip.trip.type == 'local':
            total_cost += 2
        elif ticket_trip.trip.type == 'inter-town':
            trip_cost = InterTownTrip.objects.get(trip_id=ticket_trip.trip.trip_id).route.trip_cost
            total_cost += trip_cost

    customer_id = f'Customer ID: {customer_obj.customer_id}'
    date = f'Date: {ticket.date_purchased}'
    last_name = f'Last Name: {customer_obj.last_name}'
    given_name = f'Given Name: {customer_obj.given_name}'
    middle_initial = f'Middle Initial: {customer_obj.middle_initial}'
    birth_date = f'Birth Date: {customer_obj.birth_date}'
    gender = f'Gender: {customer_obj.current_gender}'
    total_cost = f'Total Cost: {total_cost}'

    customer[customer_obj] = [customer_id, date, last_name, given_name, middle_initial, birth_date, gender, total_cost]

    context = {
        'customer' : customer,
        'trips' : trips,
    }

    return render(request, 'main/ticket_detail.html', context)

def Customers(request):

    customers_set = Customer.objects.all()

    customers = {}
    
    for customer in customers_set:
        customers[customer] = customer.birth_date

    context = {
        'customers' : customers,    
    }
    return render(request, 'main/customers.html', context)

def CustomerDetail(request, pk):

    customer = Customer.objects.get(customer_id=pk)

    tickets = Ticket.objects.filter(customer=customer)
    trips = []
    for ticket in tickets:
        for ticket_trip in ticket.tickettrip_set.all():
            trips.append(ticket_trip.trip)

    history = {}
    for trip in trips:
        train = trip.train

        if trip.type == 'local':
            route = LocalTrip.objects.get(trip_id=trip.trip_id).station
            origin = Station.objects.get(station_id=route.station_id)
            destination = Station.objects.get(station_id=route.destination.station_id)
            duration = 5
            cost = 2

        elif trip.type == 'inter-town':
            route = InterTownTrip.objects.get(trip_id=trip.trip_id).route
            origin = Station.objects.get(station_id=route.origin.station_id)
            destination = Station.objects.get(station_id=route.destination.station_id)
            duration = route.travel_time
            cost = route.trip_cost

        departure = trip.departure_time
        arrival = trip.departure_time

        history[trip] = [train.train_id, origin, destination, departure, arrival, duration, cost]

    context = {
        'customer' : customer,
        'history' : history,
    }
    return render(request, 'main/customer_detail.html', context)

def TripCreate(request, type):
    
    if request.method == 'POST':
        form = request.POST
        train = Train.objects.get(train_id=form.get('train'))

        if TripDate.objects.filter(date=form.get('date')):
            trip_date = TripDate.objects.filter(date=form.get('date'))[0]
        else:
            trip_date = TripDate(date=form.get('date'))
            trip_date.save()

        newTrip = Trip(
            train=train,
            trip_date=trip_date,
            departure_time=form.get('time'),
            type=type
        )
        newTrip.save()

        if type == 'local':
            origin = LocalStation.objects.get(station_id=form.get('route'))
            
            newLocalTrip = LocalTrip(
                trip_id = newTrip.trip_id,
                station = origin
            )
            newLocalTrip.save()

        elif type == 'inter-town':
            route = InterTownRoute.objects.get(route_id=form.get('route'))

            newInterTownTrip = InterTownTrip(
                trip_id = newTrip.trip_id,
                route = route)
            newInterTownTrip.save()
        
        return redirect("trip-date-detail", trip_date.date)
    
    trains = Train.objects.all()
    
    routes = {}
    if type == 'local':
        local_stations = LocalStation.objects.all()
        for l_s in local_stations:
            origin = Station.objects.get(station_id=l_s.station_id)
            destination = Station.objects.get(station_id=l_s.destination.station_id)
            routes[l_s.station_id] = f'{origin} to {destination}'
        
    elif type == 'inter-town':
        town_routes = InterTownRoute.objects.all()
        for t_r in town_routes:
            origin = Station.objects.get(station_id=t_r.origin.station_id)
            destination = Station.objects.get(station_id=t_r.destination.station_id)
            routes[t_r.route_id] = f'{origin} to {destination}'
        

    context = {
        'type' : type,
        'trains': trains,
        'routes' : routes,
    }

    return render(request, 'main/trip_create.html', context)

def TicketCreate(request):

    if request.method == 'POST':
        form = request.POST
        customers = Customer.objects.filter(given_name=form.get('given'),
        middle_initial=form.get('middle'),
        last_name=form.get('last'),
        birth_date=form.get('date'),
        current_gender=form.get('gender'),)
        if len(customers) > 0:
            customer = customers[0]
        else:
            customer = Customer(
                given_name=form.get('given'),
                middle_initial=form.get('middle'),
                last_name=form.get('last'),
                birth_date=form.get('date'),
                current_gender=form.get('gender'),
            )
            customer.save()

        ticket = Ticket(customer = customer)
        ticket.save()

        for key in form:
            if key.startswith('trip') and form.get(key):
                trip = Trip.objects.get(trip_id=form.get(key))
                ticket_trip = TicketTrip(
                    trip = trip,
                    ticket = ticket
                )
                ticket_trip.save()

    all_trips = Trip.objects.order_by('trip_date__date')
    trips = {}
    for trip in all_trips:
        date = trip.trip_date.date
        departure_time = trip.departure_time
        if trip.type == 'local':
            local_trip = LocalTrip.objects.get(trip_id=trip.trip_id)
            origin = Station.objects.get(
                station_id = local_trip.station.station_id
                )
            destination = Station.objects.get(
                station_id = local_trip.station.destination.station_id
                )

            arrival_time = departure_time

            cost = '5 Lion Coins'

        elif trip.type == 'inter-town':
            route = InterTownTrip.objects.get(trip_id=trip.trip_id).route
            origin = Station.objects.get(
                station_id = route.origin.station_id
                )
            destination = Station.objects.get(
                station_id = route.destination.station_id
                )

            arrival_time = departure_time

            cost = f'{route.trip_cost} Lion Coins'

        trips[trip.trip_id] = f'{date} | {origin} to {destination} | {departure_time} - {arrival_time} | {cost}'
        
    context = {
        'trips' : trips,
    }

    return render(request, 'main/ticket_create.html', context)