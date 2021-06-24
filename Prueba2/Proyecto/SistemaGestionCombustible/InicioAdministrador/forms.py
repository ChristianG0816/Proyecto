from django.db import models
from django.forms import fields, widgets
from .models import Registro, Estacion, Municipio
from django import forms

class MunicipioForms(forms.ModelForm):
    class Meta:
        model=Municipio
        fields='__all__'
        labels={
            'iddepartamento':'Departamento',
        }
        widgets={
            'iddepartamento':forms.Select(attrs={'requerid':True, 'class':'form-control'}),
        }

class EstacionForms(forms.ModelForm):
    class Meta:
        model=Estacion
        fields='__all__'
        labels={
            'idmunicipio':'Municipio',
            'nombree':'Estación',
        }
        widgets={
            'idmunicipio':forms.Select(attrs={'requerid':True, 'class':'form-control'}),
            'nombree':forms.TextInput(attrs={'class':'form-control'}),
        }

class RegistroForms(forms.ModelForm):
    class Meta:
        model=Registro
        fields=[
            'idcombustible',
            'idservicio',
            'fecharegistro', 
            'preciocombustible',
            'precioreferencia',
        ]
        labels={
            'idcombustible':'Combustible',
            'idservicio':'Servicio',
            'fecharegistro':'Fecha', 
            'preciocombustible':'Precio Combustible',
            'precioreferencia':'Precio Referencia',
        }
        widgets={
            'idcombustible':forms.Select(attrs={'requerid':True, 'class':'form-control'}),
            'idservicio':forms.Select(attrs={'requerid':True, 'class':'form-control'}),
            'fecharegistro': forms.DateInput(attrs={'type':'date', 'class':'form-control'}), 
            'preciocombustible': forms.NumberInput(attrs={'min':'1','value':'1','class':'form-control'}),
            'precioreferencia':forms.NumberInput(attrs={'min':'1','value':'1','class':'form-control'}),
        }