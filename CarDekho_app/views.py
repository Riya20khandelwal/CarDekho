from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
# from django.http import HttpResponse
# import json

from .api_file.serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# def car_list_view(request):
#     cars = Carlist.objects.all()
#     data = {
#         'cars' : list(cars.values()),
#     }
#     data_json = json.dumps(data)
#     return HttpResponse(data_json, content_type='application/json')
#     # return JsonResponse(data)


# def car_detail_view(request, pk):
#     car = Carlist.objects.get(pk=pk)
#     data = {
#         'name' : car.name,
#         'description' : car.description,
#         'active' : car.active
#     }
#     return JsonResponse(data)

@api_view()
def car_list_view(request):
    car = Carlist.objects.all()
    serializer = CarSerializer(car, many=True)
    return Response(serializer.data)


@api_view()
def car_detail_view(request, pk):
    car = Carlist.objects.get(pk=pk)
    serializer = CarSerializer(car)
    return Response(serializer.data)