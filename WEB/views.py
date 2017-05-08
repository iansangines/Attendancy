from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login as contrib_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from forms import *
from API.serializers import *
from API.models import *
from serializers import *
from models import *
from django.views.generic import ListView, TemplateView
from utils import timestamp_to_datetime
import datetime


def professor_check(user):
    try:
        p = Professor.objects.get(user_id=user.id)
    except:
        p = None
    return p is not None


def alumne_check(user):
    try:
        a = Alumne.objects.get(user_id=user.id)
    except:
        a = None
    return a is not None


def login(request):
	template_name = "login.html"
	if request.user.is_authenticated():
		return HttpResponseRedirect ('/WEB/home/')
	return contrib_login(request, template_name)

@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def home(request):
    template_name = "index.html"
    return render(request, template_name)


@login_required(login_url='/WEB/login/')
@user_passes_test(alumne_check, login_url='/WEB/home/')
def deny_alumnes(request):
    template_name = "denyalumnes.html"
    return render(request, template_name)


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def llista_alumnes(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    context = {'users': serializer.data}
    return render(request, 'users.html', context)


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def create_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            sala = Sala(nom=form.cleaned_data['name'], MAC=form.cleaned_data['MAC'])
            sala.save()
            return HttpResponseRedirect('/WEB/')
    else:
        form = SalaForm()
        return render(request, 'createSala.html', {'form': form})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def llista_sales(request):
    sales = Sala.objects.all()
    serializer = SalaSerializer(sales, many=True)
    context = {'sales': serializer.data}
    return render(request, 'sales.html', context)


def alta_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'], email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'])
            user.save()
            professor = Professor(user=user)
            professor.save()
            return HttpResponseRedirect('/WEB/')
    else:
        form = ProfessorForm()
        return render(request, 'altaProfessor.html', {'form': form})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def assistencia(request):
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    form = assistenciaForm(classesProfessor=classesProfessor)
    return render(request, 'assistencia.html', {'form': form})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def llista_assistencies(request):
    if request.method == 'GET':
        # form = assistenciaForm(request.GET)
        # data = form.diaClasse
        return render(request, 'llistaAssistencia.html',
                      {'data': request.GET.get("diaClasse"), 'classe': request.GET.get("assignaturesProfessor")})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def llista_classes_professor(request):
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    classes = []
    for classe in classesProfessor:
        #dies_classe = ""
        #dies_setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendes", "Dissabte", "Diumnege"]
        #dies = classe.dies.split(",")
        #for dia in dies:
        #    dies_classe = dies_classe + dies_setmana[int(dia)] + ", "
        #print dies_classe
        #classe.dies = dies_classe
        classes.append(classe)

    return render(request, 'llistaClassesProfessor.html', {'classes': classes})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def crear_classe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            classe = Classe(assignatura=form.cleaned_data['assignatura'],sala=form.cleaned_data['sala'],dia=form.cleaned_data['dia'], horaInici=form.cleaned_data['horaInici'], horaFinal=form.cleaned_data['horaFinal'])
            classe.save()
	    u = User.objects.get(id=request.user.id)
	    p = Professor.objects.get(user=u)
	    classeprofe = ClasseProfe(classe=classe,professor=p)
	    classeprofe.save()
            return HttpResponseRedirect('/WEB/')
    else:
        form = ClasseForm()
        return render(request, 'crearHoraris.html', {'form': form})

class CalendarJsonListView(ListView):

    template_name = 'calendar_events.html'
    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date) + datetime.timedelta(-30),
                    timestamp_to_datetime(to_date)
                    )
            )
        elif from_date:
            queryset = queryset.filter(
                start__gte=timestamp_to_datetime(from_date)
            )
        elif to_date:
            queryset = queryset.filter(
                end__lte=timestamp_to_datetime(to_date)
            )

        return event_serializer(queryset)


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/denyalumnes/')
def CalendarView(request):
    template_name = 'calendar.html'
    return render(request, template_name)
