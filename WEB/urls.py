from django.conf.urls import url
from WEB import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^users/$', views.UserPageView.as_view(), name = 'users'),
    url(r'^createSala/$', views.create_sala, name = 'createsala'),
]
