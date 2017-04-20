from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from WEB import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':"/WEB/login/"}),
    url(r'^denyalumnes/$', views.deny_alumnes, name = 'denyalumnes'),
    url(r'^users/$', views.llista_users, name = 'users'),
    url(r'^sales/$', views.llista_sales, name='sales'),
    url(r'^createSala/$', views.create_sala, name = 'createsala'),
    url(r'^altaProfessor/$', views.alta_professor, name = 'altaprofessor'),
    
]