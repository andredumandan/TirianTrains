from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView, name='home'),
    path('train-maintenance/', TrainMaintenance, name='train-maintenance'),
    path('train-maintenance/train/<str:pk>/', TrainDetail, name='train-detail'),
    path('train-routes/', TrainRoutes, name='train-routes'),
    path('train-routes/depart/<str:pk>/', DepartureRoutes, name='departure-routes'),
    path('train-routes/arrive/<str:pk>/', ArrivalRoutes, name='arrival-routes'),
    path('trip-schedules/', TripSchedules, name='trip-schedules'),
    path('trip-schedules/<str:pk>/', TripDateDetail, name='trip-date-detail'),
    path('trips/', Trips, name='trips'),
    path('ticket-sales/', TicketSales, name='ticket-sales'),
]