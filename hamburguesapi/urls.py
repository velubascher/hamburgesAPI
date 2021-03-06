"""hamburguesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import HamburguesaViewSet, IngredienteViewSet


class SlashRouter(DefaultRouter):

    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'
    
router = SlashRouter()
router.register(r'hamburguesa', HamburguesaViewSet, basename='hamburguesa')
router.register(r'ingrediente', IngredienteViewSet, basename='ingrediente')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
]
