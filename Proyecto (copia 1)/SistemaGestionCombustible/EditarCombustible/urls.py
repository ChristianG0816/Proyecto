from django.urls import path
from django.urls.resolvers import URLPattern
from .views import editarCombustible

urlpatterns = [
   path('editar/<int:pk>',editarCombustible.as_view(), name="editar")
]
