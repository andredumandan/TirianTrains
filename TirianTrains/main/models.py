# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
class Train(models.Model):
    train_id = models.AutoField(primary_key=True)
    series = models.CharField(max_length=1)
    model_number = models.IntegerField()
    max_speed = models.FloatField()
    seats = models.IntegerField()
    toilets = models.IntegerField()
    reclining_seats = models.BooleanField()
    luggage_storage = models.BooleanField()
    folding_tables = models.BooleanField()
    vending_machines = models.BooleanField()
    disability_access = models.BooleanField()
    food_services = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'train'
    
    def __str__(self) -> str:
        return f'{self.series}-{self.model_number}'

class MaintenanceCrew(models.Model):
    crew_no = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maintenance_crew'

    def __str__(self) -> str:
        return f'{self.last_name[0]}. {self.given_name}'

class MaintenanceCertificate(models.Model):
    certificate_no = models.AutoField(primary_key=True)
    train = models.OneToOneField('Train', on_delete=models.CASCADE, blank=True, null=True, related_name='maintenance_certificate')

    class Meta:
        managed = False
        db_table = 'maintenance_certificate'

    def __str__(self) -> str:
        return f'{self.train}'

class CrewCertificate(models.Model):
    crew_cert_id = models.AutoField(primary_key=True)
    crew_no = models.ForeignKey('MaintenanceCrew', on_delete=models.CASCADE, db_column='crew_no')
    certificate_no = models.ForeignKey('MaintenanceCertificate', on_delete=models.CASCADE, db_column='certificate_no')
    maintenance_date = models.DateField()
    condition = models.CharField(max_length=255)
    task = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crew_certificate'

    def __str__(self) -> str:
        return f'{self.crew_no} {self.certificate_no} {self.maintenance_date}'

class Task(models.Model):
    task_id = models.AutoField(primary_key=True) 
    crew_cert_id = models.IntegerField()
    task = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'task'

    def __str__(self) -> str:
        return f'{self.crew_cert_id}-{self.task}'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    current_gender = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self) -> str:
        return f'{self.last_name}, {self.given_name} {self.middle_initial}.'


class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default="")

    class Meta:
        managed = False
        db_table = 'station'

    def __str__(self) -> str:
        return f'{self.station_name}'

class LocalStation(models.Model):
    station_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    trip_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'local_station'

    def __str__(self) -> str:
        return f'{self.station_id}'

class TownStation(models.Model):
    station_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'town_station'

    def __str__(self) -> str:
        return f'{self.station_id}'

class InterTownRoute(models.Model):
    route_id = models.AutoField(primary_key=True)
    origin = models.ForeignKey('TownStation', on_delete=models.CASCADE, related_name='route_origin')
    destination = models.ForeignKey('TownStation', on_delete=models.CASCADE, related_name='route_destination')
    travel_time = models.FloatField(blank=True, null=True)
    trip_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inter_town_route'

    def __str__(self) -> str:
        return f'{self.origin} to {self.destination}'

class TripDate(models.Model):
    date = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'trip_date'

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    trip_date = models.ForeignKey('TripDate', on_delete=models.CASCADE, db_column='trip_date')
    departure_time = models.TimeField()
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'trip'

    def __str__(self) -> str:
        return f'{self.trip_id} {self.train} @ {self.trip_date} {self.departure_time}'

class LocalTrip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    station = models.ForeignKey(LocalStation, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'local_trip'

    def __str__(self) -> str:
        return f'{self.trip_id} {self.station}'

class InterTownTrip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(InterTownRoute, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'inter_town_trip'

    def __str__(self) -> str:
        return f'{self.route}'

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_purchased = models.DateField(default=datetime.now)

    class Meta:
        managed = False
        db_table = 'ticket'
    
    def __str__(self) -> str:
        return f'{self.ticket_id}-{self.customer}'
        
class TicketTrip(models.Model):
    ticket_trip_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ticket_trip'
    
    def __str__(self) -> str:
        return f'{self.trip}, {self.ticket}'
