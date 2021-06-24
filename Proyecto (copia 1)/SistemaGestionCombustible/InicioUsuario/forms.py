from django.db import models
from django.forms import fields, widgets
from .models import Registro, Estacion, Municipio
from django import forms

class MunicipioForms(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__' #Selecciono todos los datos de la base de datos
        labels ={
            'iddepartamento':'Departamento',
        }

        widgets={
            'iddepartamento':forms.Select(attrs={'requerid':True, 'class':'form-control'}),
        }

class EstacionForms(forms.ModelForm):
    class Meta:
        model = Estacion
        fields = '__all__'
        labels={
            'idmunicipio':'Municipio',
            'nombree':'Estacion',
        }