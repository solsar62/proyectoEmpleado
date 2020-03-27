from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('new-dept/', 
    views.NewDepartamentoView.as_view(), 
    name='nuevo_departamento'
    ),
    path('listar-dept/', 
    views.DepartamentoListView.as_view(), 
    name='listar_departamento'),
]
