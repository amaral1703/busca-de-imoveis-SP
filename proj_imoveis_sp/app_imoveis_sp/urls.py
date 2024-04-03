from django.urls import path
from . import app_views

urlpatterns = [
    path('', app_views.index, name='index'),
    path('pesquisa', app_views.pesquisa, name='mostrar_pesquisa'),

]