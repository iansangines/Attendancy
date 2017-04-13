from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('userprofiles', views.userprofiles, name='userprofiles'),
    url('alumnes', views.alumnes, name='alumnes'),
    url('professors', views.professors, name='professors'),
    url('dispositius', views.dispositius, name='dispositius'),
    url('sales', views.SalesList.as_view(), name='sales'),
    url('classes', views.classes, name='classes'),
    url('classealumne', views.classealumne, name='classealumne'),
    url('assistencies', views.assistencies, name='assistencies'),
]
