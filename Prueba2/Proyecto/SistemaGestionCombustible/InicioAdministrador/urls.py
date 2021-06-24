#Cada aplicacion manejara su url

from django.urls import path
from .views import inicioAdministrador, eliminarCombustible

urlpatterns = [
   path('inicioadmin/',inicioAdministrador.as_view(), name="inicioAdministrador"),
   path('eliminar/<int:pk>', eliminarCombustible.as_view(),name = "eliminar")

]
