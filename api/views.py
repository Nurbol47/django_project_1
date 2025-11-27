from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from .models import Car, Person


class CarView(generics.ListAPIView):
    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer


class PersonView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ApplicationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


