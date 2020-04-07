from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView
# import models
from .models import Prueba
from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'
    
class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['1', '20', '30', '40']
    

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'

    
