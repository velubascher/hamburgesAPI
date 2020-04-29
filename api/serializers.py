from rest_framework import serializers
from .models import Hamburguesa, Ingrediente
from rest_framework.exceptions import ValidationError


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self, instance):
        hamburguesa = super().to_representation(instance)
        ingredientes = hamburguesa.pop('ingredientes')
        hamburguesa['ingredientes'] = [dict(path=ing) for ing in ingredientes]
        return hamburguesa

    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        read_only_fields = ['id', 'ingredientes']

    def validate(self, data):
        if self.partial and hasattr(self, 'initial_data'):
            unknown_keys = set(self.initial_data.keys()) - set(self.fields.keys())
            if unknown_keys:
                raise ValidationError("Got unknown fields: {}".format(unknown_keys))
        return data

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']
