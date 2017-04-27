from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from WEB import views

urlpatterns = [
    url(r'^$',auth_views.login, {'template_name':'login.html'}),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':"/WEB/"}),
    url(r'^denyalumnes/$', views.deny_alumnes, name = 'denyalumnes'),
    url(r'^users/$', views.llista_users, name = 'users'),
    url(r'^sales/$', views.llista_sales, name='sales'),
    url(r'^createSala/$', views.create_sala, name = 'createsala'),
    url(r'^altaProfessor/$', views.alta_professor, name = 'altaprofessor'),
    url(r'^assistencia/$', views.assistencia, name = 'getassistencies'),
    url(r'^getAssistencies/$', views.llista_assistencies, name = 'getassistencies'),

]
