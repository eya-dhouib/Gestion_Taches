from django.shortcuts import render
from rest_framework import viewsets

from .models import Taches
from .serializers import tacheserializer

class GestionTaches(viewsets.ModelViewSet):
    queryset = Taches.objects.all()
    serializer_class = tacheserializer
    
