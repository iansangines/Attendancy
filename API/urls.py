from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('userprofiles', views.UserprofilesList.as_view(), name='userprofiles'),
    url('alumnes', views.AlumnesList.as_view(), name='alumnes'),
    url('professors', views.ProfessorsList.as_view(), name='professors'),
    url('dispositius', views.DispositiusList.as_view(), name='dispositius'),
    url('sales', views.SalesList.as_view(), name='sales'),
    url('classes', views.ClassesList.as_view(), name='classes'),
    url('classealumne', views.ClassealumneList.as_view(), name='classealumne'),
    url('assistencies', views.AssistenciesList.as_view(), name='assistencies'),
]
