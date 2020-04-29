from django.contrib import admin
from .models import Hamburguesa, Ingrediente

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(Hamburguesa)
