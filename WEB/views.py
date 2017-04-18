from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import *
from API.serializers import *

@login_required(login_url='/WEB/login/')
def home(request):
    template_name = "index.html"
    return render(request,template_name)

@login_required(login_url='/WEB/login/')
def llista_users(request):
	users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        context = {'users' : serializer.data}
	return render (request, 'users.html', context)

@login_required(login_url='/WEB/login/')
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

@login_required(login_url='/WEB/login/')
def llista_sales(request):
    sales = Sala.objects.all()
    serializer = SalaSerializer(sales, many=True)
    context = { 'sales' : serializer.data}
    return render (request, 'sales.html', context)


