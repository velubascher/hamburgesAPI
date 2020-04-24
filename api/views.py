from django.shortcuts import render
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente
from rest_framework import viewsets

# Create your views here.

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()


class HamburguesaViewSet(viewsets.ModelViewSet):
    serializer_class = HamburguesaSerializer
    queryset = Hamburguesa.objects.all()
