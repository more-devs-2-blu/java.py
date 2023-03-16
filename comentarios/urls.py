from django.urls import path
from . import views


urlpatterns = [
    path('Cadastro/', views.Cadastro, name='comentarios/cadastro'),
    path('Listagem/', views.Listagem, name='comentarios/listagem'),
]
