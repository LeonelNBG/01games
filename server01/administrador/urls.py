from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comunidad.html', views.comunidad, name='comunidad'),
    path('foro.html', views.foro, name='foro'),
]