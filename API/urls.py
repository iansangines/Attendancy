from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('altaDisp', views.altaDispositiu),
    url('altaAlumne', views.altaAlumne),
    url('alumneClasse', views.get_alumnes_classe),

]
