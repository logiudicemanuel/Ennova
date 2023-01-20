from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import TODOSerializers
from .models import TODO
from django.shortcuts import render

# Create your views here.

class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializers
