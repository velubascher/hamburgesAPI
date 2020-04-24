from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'descripcion', 'imagen', 'ingredientes']
