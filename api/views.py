from django.shortcuts import render
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .actions import format_response

# Create your views here.

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = Ingrediente.objects.all()

    def retrieve(self, request, pk=None):
        if not pk.isdigit():
            raise ValidationError('id invalido')
        ingrediente = self.get_object()
        serializer = self.get_serializer(ingrediente)
        return Response(format_response(serializer.data))

    def list(self, request):
        ingrediente = self.get_queryset()
        serializer = self.get_serializer(ingrediente, many=True)
        return Response(format_response(serializer.data))

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    def destroy(self, request, pk=None):
        ingrediente = self.get_object()
        serializer = self.get_serializer(ingrediente)
        hamburguesas = list(d['nombre'] for d in serializer.data['hamburguesas'])
        
        if hamburguesas:
            return Response(status=status.HTTP_409_CONFLICT)
        
        self.perform_destroy(ingrediente)
        return Response(status=status.HTTP_204_NO_CONTENT)


class HamburguesaViewSet(viewsets.ModelViewSet):
    serializer_class = HamburguesaSerializer
    queryset = Hamburguesa.objects.all()

    def retrieve(self, request, pk=None):
        if not pk.isdigit():
            raise ValidationError('id invalido') 
        hamburguesa = self.get_object()
        serializer = self.get_serializer(hamburguesa)
        return Response(serializer)

    def destroy(self, request, *args, **kwargs):
        hamburguesa = self.get_object()
        self.perform_destroy(hamburguesa)
        return Response(status=status.HTTP_200_OK)


