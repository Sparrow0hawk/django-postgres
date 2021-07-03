from django.urls import path 
from . import views 

urlpatterns = [
    path("<int:pk>/", views.car_details, name='car_details'),
]