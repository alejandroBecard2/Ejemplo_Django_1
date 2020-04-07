from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
DetailView,
CreateView,
TemplateView,
UpdateView,
DeleteView,
)
#models
from .models import Empleado
#forms
from .forms  import EmpleadoForm
#Requerimientos que nos han pedido
# Lista con todos los empleados de la empresa
# Listar todos los empleados que pertenecen a un área de la empresa
# Listar los empleados por palabra clave
# Listar habilidades de un empleado

class InicioView (TemplateView):
    #Vista que carga la página de inicio
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'


    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')  
        lista = Empleado.objects.filter(
            first_name__icontains= palabra_clave
         )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

class ListbyAreaEmpleado(ListView):
    """Lista empleados de un área"""
    template_name = "persona/list_area.html"
    model = Empleado
    context_object_name = 'empleados'
    

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
        departamento__name = area
    )
   
        return lista

class ListEmpleadosByKwords(ListView):
    """ Lista empleados por palabra clave"""
    template_name = 'persona/by_kword.html'

    def get_queryset(self):
        print ('*************')
        palabra_clave = self.request.GET.get("kword",' ')
        lista = Empleado.objects.filter(
        first_name = palabra_clave
         )
        return lista
    
#Listar habilidades de un empleado


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        hab_id = self.kwargs ['habil_emp']
        empleado = Empleado.objects.get(id=hab_id)
        return empleado.habilidades.all()
    

# Tarea --> Listar empleados por trabajo

class ListbyJob(ListView):
    """Lista empleados por trabajo"""
    template_name = "persona/list_job.html"
    model = Empleado


    def get_queryset(self):
        puesto = self.kwargs['puesto']
        lista = Empleado.objects.filter(
        job = puesto
    )
        return lista



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #toot un proceso 
        context ['titulo'] = 'Empleado del mes'
        return context
    


class SuccesView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #Logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',

    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('-------------------------metodo post-----------')
        print('-----------------------------------')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #Logica del proceso
        print('-------------------------metodo formvalid-----------')
        print('-----------------------------------')

        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

    

