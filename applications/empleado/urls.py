from django.contrib import admin
from django.urls import path

from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path('listar_all_empleados/', 
        views.ListAllEmpleados.as_view(),
        name='all_empleados'
    ),
    path('listar_empleados_admin/', 
        views.ListaEmpleadosAdmin.as_view(),
        name='admin_empleados'
    ),
    path('listar_por_area/<namearea>', 
        views.ListByArea.as_view(),
        name='lista_por_area'
    ),
    path('listar_por_clave/', views.ListEmpleadosKword.as_view()),
    path('listar_habilidades/', views.ListHabilidades.as_view()),
    path('listar_por_trabajo/<namejob>', views.ListByJob.as_view()),
    path('detalle-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='detalle_empleado'
    ),
    path('crear-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='nuevo_empleado'
    ),
    path(
        'success/',
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'modificar-empleado/<pk>',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'borrar-empleado/<pk>',
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    )
]