from django.shortcuts import render
from django.views.generic import TemplateView 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from forms import *
from API.serializers import *


class HomePageView(TemplateView):
    template_name = "index.html"

class UserPageView(TemplateView):
    def get (self, request, **kwargs):
	users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        context = {'users' : serializer.data}
	return render (request, 'users.html', context)

def create_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
		sala = Sala(nom = form.cleaned_data['name'], MAC = form.cleaned_data['MAC'])
		sala.save()
		return HttpResponseRedirect('/WEB/')
    else:
        form = SalaForm()
	return render(request,'createSala.html', {'form':form})

