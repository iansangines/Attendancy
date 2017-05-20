from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url('altaDisp', views.altaDispositiu),
    # url('altaAlumne', views.altaAlumne),
    # url('alumneClasse', views.get_alumnes_classe),
    url('^classes/$', views.get_alumnesClasse),
    url('^classes/(?P<id_classe>[0-9]{2})/assistencia/(?P<mac_dispositiu>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))/$',
        views.Assistencies.as_view(), name="assistencia"),
    url('^dispositius/(?P<mac>([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))/codi/$', views.getCodi),
    url('^alumnes/$', views.altaAlumne),
    url('^alumnes/(?P<username>([A-z0-9.-])+)/dispositiu/$', views.altaDispositiu),
    url('^assignatures/(?P<codiassig>([A-z0-9]{32}))/alumnes/(?P<username>([A-z0-9.-])+)/$', views.alumneAssignatura),

]
