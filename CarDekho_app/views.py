from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
from django.http import HttpResponse
import json

# Create your views here.
def car_list_view(request):
    cars = Carlist.objects.all()
    data = {
        'cars' : list(cars.values()),
    }
    data_json = json.dumps(data)
    return HttpResponse(data_json, content_type='application/json')
    # return JsonResponse(data)


def car_detail_view(request, pk):
    car = Carlist.objects.get(pk=pk)
    data = {
        'name' : car.name,
        'description' : car.description,
        'active' : car.active
    }
    return JsonResponse(data)