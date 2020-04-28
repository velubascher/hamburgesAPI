from rest_framework import serializers
from .models import Hamburguesa, Ingrediente


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, instance):
        hamburguesa = super().to_representation(instance)
        ingredientes = hamburguesa.pop('ingredientes')
        hamburguesa['ingredientes'] = [dict(path=ing) for ing in ingredientes]
        return hamburguesa

    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']
