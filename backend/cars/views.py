from django.shortcuts import render

from cars.models import Car, Driver

def car_details(request, pk):

    owner_obj = Driver.objects.get(pk=pk)

    car_objs = Car.objects.filter(owner_id = owner_obj.id)

    context = {
        "vehicles" : car_objs,
        "drivers" : owner_obj
    }

    return render(request, "car_details.html", context)