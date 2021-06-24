from django.urls import path
from .views import inicioUsuario

urlpatterns = [
    #path('',views.InicioUsuario,name="InicioUsuario"),
    path('',inicioUsuario.as_view(), name="InicioUsuario")

]