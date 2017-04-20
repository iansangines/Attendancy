from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('users', views.UsersList.as_view(), name='users'),
    url('userprofiles', views.UserprofilesList.as_view(), name='userprofiles'),
    url('alumnes', views.AlumnesList.as_view(), name='alumnes'),
    url('professors', views.ProfessorsList.as_view(), name='professors'),
    url('dispositius', views.DispositiusList.as_view(), name='dispositius'),
    url('sales', views.SalesList.as_view(), name='sales'),
    url('classes', views.ClassesList.as_view(), name='classes'),
    url('classealumne', views.ClassealumneList.as_view(), name='classealumne'),
    url('assistencies', views.AssistenciesList.as_view(), name='assistencies'),
    url('altaDisp', views.altaDispositiu),
    url('altaAlumne', views.altaAlumne),
    url('alumnesClasse', views.get_alumnes_classe),

]
