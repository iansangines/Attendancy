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

def admin_check(user):
    try:
        aa = Admin.objects.get(user_id=user.id)
    except:
        aa = None
    return aa is not None


def login(request):
    template_name = "login.html"
    if request.user.is_authenticated():
    	if admin_check(request.user):
		return HttpResponseRedirect('/WEB/sysadmin/')
        if professor_check(request.user):
        	return HttpResponseRedirect('/WEB/profe/')
	if alumne_check(request.user):
		return HttpResponseRedirect('/WEB/nonauthorized/')
    return contrib_login(request, template_name)

def non_authorized(request):
    template_name = "nonauthorized.html"
    return render(request, template_name)


@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def home_admin(request):
    template_name = "sysadmin/index.html"
    return render(request, template_name)

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def llista_alumnes(request):
    users = User.objects.all()
    alumnes = Alumne.objects.all()
    alumnesres = []
    for user in users:
	for alumne in alumnes:
		if alumne.user == user:
			alumnesres.append(alumne)
    return render(request, 'sysadmin/alumnes.html', {'alumnes':alumnesres})

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def llista_professors(request):
    users = User.objects.all()
    professors = Professor.objects.all()
    proferes = []
    for user in users:
	for professor in professors:
		if professor.user == user:
			proferes.append(professor)
    return render(request, 'sysadmin/professors.html', {'professors':proferes})

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def llista_sales(request):
    sales = Sala.objects.all()
    serializer = SalaSerializer(sales, many=True)
    context = {'sales': serializer.data}
    return render(request, 'sysadmin/sales.html', context)

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def llista_assignatures(request):
    assignatures = Assignatura.objects.all()
    serializer = AssignaturaSerializer(assignatures, many=True)
    context = {'assignatures': serializer.data}
    return render(request, 'sysadmin/assignatures.html', context)

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def llista_classes_assignatura(request):
    assignatura = request.GET.get('assignatura')
    classes = Classe.objects.all()
    classesres = []
    for classe in classes:
	if classe.assignatura.nom == assignatura:
		classesres.append(classe)
    return render(request, 'sysadmin/classes.html', {'classes':classesres})

# @login_required(login_url='/WEB/login/')
# @user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
# def crear_classe(request):
#     if request.method == 'POST':
#         form = ClasseForm(request.POST)
#         if form.is_valid():
#             classe = Classe(assignatura=form.cleaned_data['assignatura'],sala=form.cleaned_data['sala'],dia=form.cleaned_data['dia'], horaInici=form.cleaned_data['horaInici'], horaFinal=form.cleaned_data['horaFinal'])
# 	    u = User.objects.get(id=request.user.id)
# 	    p = Professor.objects.get(user=u)
# 	    classeprofe = ClasseProfe(classe=classe,professor=p)
# 	    #ce = CalendarEvent(title=classe.assignatura.nom,url='/WEB/',start=,end=)
#             classe.save()
#             classeprofe.save()
#             #ce.save()
#             return HttpResponseRedirect('/WEB/admin/')
#     else:
#         form = ClasseForm()
#         return render(request, 'crearHoraris.html', {'form': form, 'diesSetmana': range(0, 5), 'horesDia': range(8, 21)})

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def crear_classe(request):
    if request.method == 'POST':
        # something
        horari = request.POST.getlist('horari')
        print(horari)
        return HttpResponseRedirect('/WEB/sysadmin')

    else:
        form = ClasseForm()
        return render(request, 'sysadmin/crearHoraris.html',
                      {'form': form, 'diesSetmana': range(0, 5), 'horesDia': range(8, 21)})

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def crear_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            sala = Sala(nom=form.cleaned_data['name'], MAC=form.cleaned_data['MAC'])
            sala.save()
            return HttpResponseRedirect('/WEB/sysadmin/sales')
    else:
        form = SalaForm()
        return render(request, 'sysadmin/createSala.html', {'form': form})

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def alta_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'], email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'])
            a = Admin.objects.get(user_id=request.user.id)
	    uni = a.uni
            professor = Professor(user=user,uni=uni)
            user.save()
            professor.save()
            return HttpResponseRedirect('/WEB/sysadmin/professors')
    else:
        form = ProfessorForm()
        return render(request, 'sysadmin/altaProfessor.html', {'form': form})

@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def delete(request):
	profenom = request.GET.get('professor')
        alumnenom = request.GET.get('alumne')
	salanom = request.GET.get('sala')
        assignom = request.GET.get('assignatura')
        if profenom is not None:
		user = User.objects.get(username=profenom)
		user.delete()
	        return HttpResponseRedirect('/WEB/sysadmin/professors')
        if alumnenom is not None:
		user = User.objects.get(username=alumnenom)
		user.delete()
	        return HttpResponseRedirect('/WEB/sysadmin/alumnes')
        elif salanom is not None:
		sala = Sala.objects.get(nom=salanom)
		sala.delete()
	        return HttpResponseRedirect('/WEB/sysadmin/sales')
        elif assignom is not None:
		assignatura = Assignatura.objects.get(nom=assignom)
		assignatura.delete()
	        return HttpResponseRedirect('/WEB/sysadmin/assignatures')
        

@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def home_profe(request):
    template_name = "profe/index.html"
    return render(request, template_name)

def __eq__(self, other): 
        return self.__dict__ == other.__dict__
 
@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def llista_alumnes_professor(request):
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    users = []
    for classe in classesProfessor:
	alumnes = Alumne.objects.all()
	for alumne in alumnes:
		classesAlumne = Classe.objects.filter(classealumne__alumne=alumne)
		for classe2 in classesAlumne:
			if classe == classe2:
				users.append(alumne.user)
	

    return render(request, 'profe/alumnes.html', {'users':users})

@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def llista_assignatures_professor(request):
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    assignaturesres = []
    for classe in classesProfessor:
	assignatures = Assignatura.objects.all()
	for assig in assignatures:
		if classe.assignatura == assig:
			assignaturesres.append(assig)
    return render(request, 'profe/assignatures.html', {'assignatures':assignaturesres})
 
@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def llista_classes_assignatura_professor(request):
    assignatura = request.GET.get('assignatura')
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    classes = []
    for classe in classesProfessor:
        # dies_classe = ""
        # dies_setmana = ["Dilluns", "Dimarts", "Dimecres", "Dijous", "Divendes", "Dissabte", "Diumnege"]
        # dies = classe.dies.split(",")
        # for dia in dies:
        #    dies_classe = dies_classe + dies_setmana[int(dia)] + ", "
        # print dies_classe
        # classe.dies = dies_classe
        if classe.assignatura.nom == assignatura:
        	classes.append(classe)

    return render(request, 'profe/llistaClassesProfessor.html', {'classes': classes})


class CalendarJsonListView(ListView):
    template_name = 'profe/calendar_events.html'

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
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def CalendarView(request):
    template_name = 'profe/calendar.html'
    return render(request, template_name)

@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def assistencia(request):
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    form = assistenciaForm(classesProfessor=classesProfessor)
    return render(request, 'profe/assistencia.html', {'form': form})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def llista_assistencies(request):
    if request.method == 'GET':
        # form = assistenciaForm(request.GET)
        # data = form.diaClasse
        return render(request, 'profe/llistaAssistencia.html',
                      {'data': request.GET.get("diaClasse"), 'classe': request.GET.get("assignaturesProfessor")})

