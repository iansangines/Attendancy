from django.shortcuts import render
from django.views.generic import TemplateView 
from API.serializers import UserSerializer
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = "index.html"

class UserPageView(TemplateView):
    def get (self, request, **kwargs):
	users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        context = {'users' : serializer.data}
	return render (request, 'users.html', context)
