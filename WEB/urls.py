from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from WEB import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/$', views.login),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':"/WEB/"}),
    url(r'^nonauthorized/$', views.non_authorized, name = 'nonauthorized'),
    url(r'^sysadmin/$', views.home_admin, name='homeadmin'),
    url(r'^sysadmin/professors/$', views.llista_professors, name='professors'),
    url(r'^sysadmin/alumnes/$', views.llista_alumnes, name='alumnes'),
    url(r'^sysadmin/sales/$', views.llista_sales, name='sales'),
    url(r'^sysadmin/assignatures/$', views.llista_assignatures, name='assignatures'),
    url(r'^sysadmin/classesassignatura/$', views.llista_classes_assignatura, name='classesassignatura'),
    url(r'^sysadmin/crearclasse/', views.crear_classe, name ='crearclasse'),
    url(r'^sysadmin/crearsala/$', views.crear_sala, name = 'createsala'),
    url(r'^sysadmin/altaprofessor/$', views.alta_professor, name = 'altaprofessor'),
    url(r'^sysadmin/delete/$', views.delete, name = 'delete'),
    url(r'^profe/$', views.home_profe, name='homeprofe'),
    url(r'^profe/alumnesprofessor/$', views.llista_alumnes_professor, name = 'alumnesprofessor'),
    url(r'^profe/assigsprofessor/$', views.llista_assignatures_professor, name = 'assigsprofessor'), 
    url(r'^profe/classesassigprofessor/$', views.llista_classes_assignatura_professor, name = 'classesassigprofessor'), 
    url(r'^profe/json/$', views.CalendarJsonListView.as_view(), name='calendar_json'),
    url(r'^profe/calendar/', views.CalendarView, name ='calander'), 

]
