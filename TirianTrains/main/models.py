# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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

class MaintenanceCrew(models.Model):
    crew_no = models.AutoField(primary_key=True)
    crew_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maintenance_crew'

class MaintenanceCertificate(models.Model):
    certificate_no = models.AutoField(primary_key=True)
    train = models.ForeignKey('Train', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'maintenance_certificate'

class CrewCertificate(models.Model):
    crew_cert_id = models.AutoField(primary_key=True)
    crew_no = models.ForeignKey('MaintenanceCrew', on_delete=models.CASCADE, db_column='crew_no')
    certificate_no = models.ForeignKey('MaintenanceCertificate', on_delete=models.CASCADE, db_column='certificate_no')
    maintenance_date = models.DateField()
    condition = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crew_certificate'

class Task(models.Model):
    crew_cert_id = models.IntegerField()
    task = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'task'

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

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_purchased = models.DateField()

    class Meta:
        managed = False
        db_table = 'ticket'

class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'station'

class LocalStation(models.Model):
    l_station_id = models.IntegerField(primary_key=True)
    destination = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    trip_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'local_station'

class TownStation(models.Model):
    t_station_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'town_station'

class InterTownRoute(models.Model):
    route_id = models.AutoField(primary_key=True)
    origin = models.ForeignKey('TownStation', on_delete=models.CASCADE, related_name='route_origin')
    destination = models.ForeignKey('TownStation', on_delete=models.CASCADE, related_name='route_destination')
    travel_time = models.FloatField(blank=True, null=True)
    trip_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inter_town_route'

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    trip_date = models.DateField()
    type = models.CharField(max_length=255)
    departure_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'trip'

class LocalTrip(models.Model):
    trip_id = models.IntegerField(primary_key=True)
    station = models.ForeignKey(LocalStation, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'local_trip'

class InterTownTrip(models.Model):
    trip_id = models.IntegerField(primary_key=True)
    route = models.ForeignKey(InterTownRoute, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'inter_town_trip'

class TicketTrip(models.Model):
    ticket_trip_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ticket_trip'
