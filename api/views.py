from django.shortcuts import render
from .serializers import HamburguesaSerializer, IngredienteSerializer
from .models import Hamburguesa, Ingrediente
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError, NotFound, ParseError
from rest_framework.response import Response
from .actions import format_response
from rest_framework.decorators import action

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
        return Response(status=status.HTTP_200_OK)


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

    @action(detail=True, methods=['delete', 'put'], url_path='ingrediente/(?P<ingrediente_pk>[^/.]+)')
    def ingrediente(self, request, ingrediente_pk, pk=None):
        metodo = self.request.method.lower()
        try:
            hamburguesa = self.get_object()
        except Exception:
            raise ParseError('id de hamburguesa invalido')

        try:
            ingrediente = Ingrediente.objects.get(id=ingrediente_pk)
            if metodo == 'delete' and ingrediente not in hamburguesa.ingredientes.all():
                raise NotFound
        except Exception:
            raise NotFound('Ingrediente inexistente')
            
        if self.request.method.lower() == 'delete':
            hamburguesa.ingredientes.remove(ingrediente)
        if self.request.method.lower() == 'put':
            hamburguesa.ingredientes.add(ingrediente)
        return Response(status=status.HTTP_200_OK)



