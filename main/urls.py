from django.urls import path
from . import views

urlpatterns = [
    path('Manual/', views.Manual, name='manual'),
    path('', views.Home, name='home'),
]

