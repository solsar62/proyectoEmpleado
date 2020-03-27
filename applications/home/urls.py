from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('tabla/', views.ListarPrueba.as_view()),
    path('crear/', views.PruebaCreateView.as_view(),name='prueba_add'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(),name='resume_foundation'),
]