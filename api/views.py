from django.db.models.query import QuerySet
from api import serializers
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import PictureSerializer,HomeSerializer
from .models import Picture, Home

class PictureView(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()

class HomeView(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()