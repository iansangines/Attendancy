from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('alumnes', views.alumnes, name='alumnes'),
    url('professors', views.professors, name='professors'),
    url('dispositius', views.dispositius, name='dispositius'),
    url('salas', views.salas, name='salas'),
    url('classes', views.classes, name='classes'),
    url('classesalumnes', views.classesalumnes, name='classesalumnes'),
    url('assistencies', views.assistencies, name='assistencies'),
]
