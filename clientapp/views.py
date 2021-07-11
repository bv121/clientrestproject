
from django.shortcuts import render
from apiapp.serializers import ClientSerializers,ProjectSerializers

from .models import Client,Project
from rest_framework import generics


class Createclient(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers

class ClientList(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializers

    #create project related

class ProjectCreate(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ProjectSerializers

class ProjectList(generics.ListAPIView):
    queryset=Client.objects.all()
    serializer_class=ProjectSerializers

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ProjectSerializers








