from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

#inicio


class InicioView(TemplateView):
    template_name = "inicio.html"
    

# 1- Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_admin.html'
    paginate_by = 7
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado

# 2- Listar todos los empleados que pertenecen a un area de la empresa
class ListByArea(ListView):
    template_name = 'empleado/list_byarea.html'
    context_object_name = 'empleados'
    

    def get_queryset(self):
        area = self.kwargs['namearea']
        lista = Empleado.objects.filter(
        departamento__short_name=area
    )
        return lista


# 4- Listar los empleados por palabra clave
class ListEmpleadosKword(ListView):
    template_name = 'empleado/by_kword.html'
    context_object_name='empleados'

    def get_queryset(self):
        print('*****************')
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        return lista

# 5- Listar habilidades de un empleado

class ListHabilidades(ListView):
    template_name ='empleado/lista_habilidades.html'
    context_object_name ='habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        return empleado.habilidades.all()
    
# 3- Listar empleados por trabajo
class ListByJob(ListView):
    template_name = 'empleado/list_byjob.html'
    context_object_name = 'empleados'
    

    def get_queryset(self):
        trabajo = self.kwargs['namejob']
        lista = Empleado.objects.filter(
        job=trabajo
    )
        return lista

# DetailView

class EmpleadoDetailView(DetailView):
    template_name = "empleado/detail_view.html"
    model = Empleado

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

# CreateView


class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "empleado/crear_empleado.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:admin_empleados')
    
    def form_valid(self, form):
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

# UpdateView

class EmpleadoUpdateView(UpdateView):
    template_name = "empleado/modificar.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        ]
    success_url = reverse_lazy('empleado_app:admin_empleados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        
        return super(EmpleadoUpdateView, self).form_valid(form)

# DeleteView


class EmpleadoDeleteView(DeleteView):
    template_name = "empleado/borrar.html"
    model = Empleado
    success_url = reverse_lazy('empleado_app:admin_empleados')



    
