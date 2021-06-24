from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Departamento, Municipio, Registro, Estacion
from agregar.forms import EstacionForms, MunicipioForms, RegistroForms
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import render

class agregar(CreateView):
    model=Registro
    template_name='agregar.html'
    form_class=RegistroForms
    second_form_class=EstacionForms
    third_form_class=MunicipioForms
    success_url=reverse_lazy('Agregar')
    def get_context_data(self, **kwargs):
        context=super(agregar,self).get_context_data(**kwargs)
        if 'registro' not in context:
            context['registro']=self.form_class(self.request.GET)
        if 'estacion' not in context:
            context['estacion']=self.second_form_class(self.request.GET) 
        return context
    def post(self, request, *args, **kwargs):
        registro=self.form_class(request.POST)
        estacion=self.second_form_class(request.POST)
        if registro.is_valid():
            if estacion.is_valid():
                self.object=self.get_object
                solicitud=registro.save(commit=False)
                solicitud.nombree=estacion.save()
                solicitud.save()
                return HttpResponseRedirect(self.success_url)
            else:
                solicitud=registro.save(commit=False)
                solicitud.nombree=Estacion.objects.get(nombree=estacion.data['nombree'])
                solicitud.save()
                return HttpResponseRedirect(self.success_url)
        else:            
            return self.render_to_response(self.get_context_data(registro=registro,))

def selectDinamico(request):
    listdepartamento=Departamento.objects.all()
    listmunicipio=Municipio.objects.all()
    return render(request,'agregar.html',{"departamento":listdepartamento, "municipio":listmunicipio})