from django.shortcuts import render
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

# Create your views here.

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()


class HamburguesaViewSet(viewsets.ModelViewSet):
    serializer_class = HamburguesaSerializer
    queryset = Hamburguesa.objects.all()

    def retrieve(self, request, pk=None):
        if not pk.isdigit():
            raise ValidationError('id invalido') 
        hamburguesa = self.get_object()
        serializer = self.get_serializer(hamburguesa)
        return Response(serializer.data)


