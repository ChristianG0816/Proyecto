from django.urls import path
from .views import agregar

urlpatterns = [
    path('agregar/',agregar.as_view(), name='Agregar'),
]