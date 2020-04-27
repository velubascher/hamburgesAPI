from django.shortcuts import render
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

# Create your views here.

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()

    def retrieve(self, request, pk=None):
        if not pk.isdigit():
            raise ValidationError('id invalido') 
        ingrediente = self.get_object()
        serializer = self.get_serializer(ingrediente)
        return Response(serializer.data)


class HamburguesaViewSet(viewsets.ModelViewSet):
    serializer_class = HamburguesaSerializer
    queryset = Hamburguesa.objects.all()

    def retrieve(self, request, pk=None):
        if not pk.isdigit():
            raise ValidationError('id invalido') 
        hamburguesa = self.get_object()
        serializer = self.get_serializer(hamburguesa)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        hamburguesa = self.get_object()
        self.perform_destroy(hamburguesa)
        return Response(status=status.HTTP_200_OK)


