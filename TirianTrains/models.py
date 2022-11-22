# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CrewCertificate(models.Model):
    crew_cert_id = models.AutoField(primary_key=True)
    crew_no = models.ForeignKey('MaintenanceCrew', models.DO_NOTHING, db_column='crew_no')
    certificate_no = models.ForeignKey('MaintenanceCertificate', models.DO_NOTHING, db_column='certificate_no')
    maintenance_date = models.DateField()
    condition = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crew_certificate'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    current_gender = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InterTownRoute(models.Model):
    route_id = models.AutoField(primary_key=True)
    origin = models.ForeignKey('TownStation', models.DO_NOTHING)
    destination = models.ForeignKey('TownStation', models.DO_NOTHING)
    travel_time = models.FloatField(blank=True, null=True)
    trip_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inter_town_route'


class InterTownTrip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(InterTownRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inter_town_trip'


class LocalStation(models.Model):
    l_station_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    trip_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'local_station'


class LocalTrip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    station = models.ForeignKey(LocalStation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'local_trip'


class MaintenanceCertificate(models.Model):
    certificate_no = models.AutoField(primary_key=True)
    train = models.ForeignKey('Train', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'maintenance_certificate'


class MaintenanceCrew(models.Model):
    crew_no = models.AutoField(primary_key=True)
    crew_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maintenance_crew'


class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'station'


class Task(models.Model):
    crew_cert_id = models.IntegerField()
    task = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'task'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    date_purchased = models.DateField()

    class Meta:
        managed = False
        db_table = 'ticket'


class TicketTrip(models.Model):
    ticket_trip_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('Trip', models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticket_trip'


class TownStation(models.Model):
    t_station_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'town_station'


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


class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    train = models.ForeignKey(Train, models.DO_NOTHING)
    trip_date = models.DateField()
    type = models.CharField(max_length=255)
    departure_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'trip'
