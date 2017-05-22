from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login as contrib_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from forms import *
from API.serializers import *
from API.models import *
from serializers import *
from models import *
from django.views.generic import ListView, TemplateView
from utils import timestamp_to_datetime
from datetime import datetime, timedelta
from itertools import chain


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
    return render(request, 'sysadmin/alumnes.html', {'alumnes': alumnesres})


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
    return render(request, 'sysadmin/professors.html', {'professors': proferes})


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
    context = {'assignatures': assignatures}
    return render(request, 'sysadmin/assignatures.html', context)


@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def llista_classes_assignatura(request):
    assignatura = request.GET.get('assignatura')
    classes = Classe.objects.all().order_by('dia')
    classesres = []
    for classe in classes:
        if classe.assignatura.nom == assignatura:
            classesres.append(classe)
    return render(request, 'sysadmin/classes.html', {'classes': classesres})


@login_required(login_url='/WEB/login/')
@user_passes_test(admin_check, login_url='/WEB/nonauthorized/')
def crear_classe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        dies = {'0': 'dilluns', '1': 'dimarts', '2': 'dimecres', '3': 'dijous', '4': 'divendres', '5': 'dissabte',
                '6': 'diumenge'}
        horaris = request.POST.getlist('horari')  # llistat dels values dels checkboxes apretats
        if form.is_valid():
            nomassig = form.cleaned_data['nom']
            dinici = form.cleaned_data['inici']
            dfinal = form.cleaned_data['final']
            codiassig = get_random_string(length=32)
            a = Assignatura(codiassig=codiassig, nom=nomassig, inici=dinici, final=dfinal)
            a.save();
        classes = []
        for horari in horaris:
            diaihora = horari.split(";")
            dia = dies[diaihora[0]]
            horainici = datetime.strptime(diaihora[1], '%H:%M')
            horafinal = horainici + timedelta(hours=1)
            horainici = horainici.time()
            horafinal = horafinal.time()
            try:
                if form.is_valid():
                    sala = Sala.objects.get(nom=form.cleaned_data['sala'])
                    professor = Professor.objects.get(user__username=form.cleaned_data['professor'].user.username)
                    classe = Classe(assignatura=a, sala=sala, dia=dia, horaInici=horainici,
                                    horaFinal=horafinal)
                    classes.append(classe)

                else:
                    print "no valid"
            except ValueError:
                print ValueError
                return HttpResponseRedirect('/WEB/denyalumne')

        classesdilluns = []
        classesdimarts = []
        classesdimecres = []
        classesdijous = []
        classesdivendres = []
        for classe in classes:
            if classe.dia == 'dilluns':
                classesdilluns.append(classe)
            elif classe.dia == 'dimarts':
                classesdimarts.append(classe)
            elif classe.dia == 'dimecres':
                classesdimecres.append(classe)
            elif classe.dia == 'dijous':
                classesdijous.append(classe)
            elif classe.dia == 'divendres':
                classesdivendres.append(classe)

        classes = []
        if len(classesdilluns) > 0:
            horainici = classesdilluns[0].horaInici
            horafinal = classesdilluns[len(classesdilluns) - 1].horaFinal
            classe = Classe(assignatura=a, sala=sala, dia='dilluns', horaInici=horainici, horaFinal=horafinal)
            classes.append(classe)
        if len(classesdimarts) > 0:
            horainici = classesdimarts[0].horaInici
            horafinal = classesdimarts[len(classesdimarts) - 1].horaFinal
            classe = Classe(assignatura=a, sala=sala, dia='dimarts', horaInici=horainici, horaFinal=horafinal)
            classes.append(classe)
        if len(classesdimecres) > 0:
            horainici = classesdimecres[0].horaInici
            horafinal = classesdimecres[len(classesdimecres) - 1].horaFinal
            classe = Classe(assignatura=a, sala=sala, dia='dimecres', horaInici=horainici, horaFinal=horafinal)
            classes.append(classe)
        if len(classesdijous) > 0:
            horainici = classesdijous[0].horaInici
            horafinal = classesdijous[len(classesdijous) - 1].horaFinal
            classe = Classe(assignatura=a, sala=sala, dia='dijous', horaInici=horainici, horaFinal=horafinal)
            classes.append(classe)
        if len(classesdivendres) > 0:
            horainici = classesdivendres[0].horaInici
            horafinal = classesdivendres[len(classesdivendres) - 1].horaFinal
            classe = Classe(assignatura=a, sala=sala, dia='divendres', horaInici=horainici, horaFinal=horafinal)
            classes.append(classe)

        for classe in classes:
            data = dinici;
            classe.save()
            while data <= dfinal:
                if dies[str(datetime.weekday(data))] == classe.dia:
                    start = datetime.combine(data, classe.horaInici)
                    end = datetime.combine(data, classe.horaFinal)
                    url = "/WEB/profe/assistenciaclasse?classe=" + str(classe.id) + "&data=" + str(start)
                    ce = CalendarEvent(title=a.nom, url=url, start=start, end=end)
                    ce.save()
                data = data + timedelta(days=1)
            cp = ClasseProfe(classe=classe, professor=professor)
            cp.save()
        return HttpResponseRedirect('/WEB/sysadmin/assignatures')

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
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            a = Admin.objects.get(user_id=request.user.id)
            uni = a.uni
            professor = Professor(user=user, uni=uni)
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
        ce = CalendarEvent.objects.all()
        for event in ce:
            if event.title == assignom:
                event.delete()
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
    assignatura = request.GET.get('assignatura')
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
    users = []
    assigs = []
    for classe in classesProfessor:
        alumnes = Alumne.objects.all()
        for alumne in alumnes:
            classesAlumne = Classe.objects.filter(classealumne__alumne=alumne)
            for classe2 in classesAlumne:
                if classe == classe2:
                    if classe2.assignatura.nom == assignatura:
                        if not alumne in users:
                            users.append(alumne)

    return render(request, 'profe/alumnes.html', {'users': users, 'assig': assignatura})


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
                if not assig in assignaturesres:
                    assignaturesres.append(assig)
    return render(request, 'profe/assignatures.html', {'assignatures': assignaturesres})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized/')
def llista_classes_assignatura_professor(request):
    assignatura = request.GET.get('assignatura')
    userProfessor = User.objects.get(id=request.user.id)
    professor = Professor.objects.get(user=userProfessor)
    classesProfessor = Classe.objects.filter(classeprofe__professor=professor).order_by('dia')
    classes = []
    for classe in classesProfessor:
        if classe.assignatura.nom == assignatura:
            classes.append(classe)

    return render(request, 'profe/llistaClassesProfessor.html', {'classes': classes})


class CalendarJsonListView(ListView):
    template_name = 'profe/calendar_events.html'

    def get_queryset(self):

        userProfessor = User.objects.get(id=self.request.user.id)
        professor = Professor.objects.get(user=userProfessor)
        classesProfessor = Classe.objects.filter(classeprofe__professor=professor)
        assignaturesres = []
        for classe in classesProfessor:
            assignatures = Assignatura.objects.all()
            for assig in assignatures:
                if classe.assignatura == assig:
                    if not assig in assignaturesres:
                        assignaturesres.append(assig)
        cont = 0;
        for assig in assignaturesres:
            if cont == 0:
                queryset = CalendarEvent.objects.filter(title=assig.nom)
            else:
                queryset = CalendarEvent.objects.filter(title=assig.nom) | prevqueryset
            prevqueryset = queryset
            cont = cont + 1

        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date and to_date:
            queryset = queryset.filter(
                start__range=(
                    timestamp_to_datetime(from_date) + timedelta(-30),
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
@user_passes_test(professor_check, login_url='/WEB/nonauthorized')
def historial_alumne(request):
    user = User.objects.get(username=request.GET.get('alumne'))
    alumne = Alumne.objects.get(user=user)
    assignatura = Assignatura.objects.get(nom=request.GET.get('assignatura'))
    events = CalendarEvent.objects.filter(title=assignatura.nom, start__lt=datetime.now()).order_by('start')

    classes = Classe.objects.filter(assignatura=assignatura)
    classesAlumne = ClasseAlumne.objects.filter(alumne=alumne)
    cas = []
    for ca in classesAlumne:
        for classe in classes:
            if ca.classe == classe:
                cas.append(ca)
    cont = 0
    for ca in cas:
        if cont == 0:
            assistencies = Assistencia.objects.filter(classeAlumne=ca)
        else:
            assistencies = Assistencia.objects.filter(classeAlumne=ca) | prev
        prev = assistencies
        cont = cont + 1
    cont = 0
    horesdeclasse = 0
    horesassistides = 0
    events_assistits = []
    for event in events:
        durada = event.end - event.start
	estada = event.end - event.end
        for assist in assistencies:
            if assist.data == event.start.date():
		if assist.sortida is None:
			assist.sortida = datetime.now().time()
			print assist.sortida
                if assist.entrada >= event.start.time() and assist.sortida <= event.end.time():
		    entrada = datetime.combine(event.start, assist.entrada)
                    sortida = datetime.combine(event.start, assist.sortida)
               	    estada += sortida - entrada
		    
        if cont == 0:
            horesclasse = durada
            horesassistides = estada
        else:
            horesclasse += durada
            horesassistides += estada

	event_assistit = {'event':event,'durada':durada,'estada':estada}
	events_assistits.append(event_assistit)

        cont += 1

    horesclasse = horesclasse.days * 24.00 + horesclasse.seconds / 3600.00
    horesassistides = horesassistides.days*24.00 + horesassistides.seconds / 3600.00
    percentatge = horesassistides / horesclasse * 100.00
    return render(request, 'profe/historialAlumne.html', {'assignatura': assignatura, 'events': events_assistits, 'horesclasse':horesclasse,'horesassistides':horesassistides,'percentatge':percentatge})


@login_required(login_url='/WEB/login/')
@user_passes_test(professor_check, login_url='/WEB/nonauthorized')
def assistencia_classe(request):
    classe = request.GET.get('classe')
    data = request.GET.get('data')

    classe = int(classe)
    data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    data = data.date()

    classe = Classe.objects.get(id=classe)

    cas = ClasseAlumne.objects.filter(classe=classe)

    alumnesAssistents = []
    not_assistencies = []
    datactual = datetime.now()
    if data <= datactual.date():
    	for ca in cas:
    	    print(ca.alumne.user.username)
    	    print(data)
    	    assistenciesAlumne = Assistencia.objects.filter(classeAlumne=ca, data=data)
	    if not assistenciesAlumne:
		not_assistencies.append(ca.alumne)
	    for a in assistenciesAlumne:
    	        a.entrada = a.entrada.isoformat()
		if a.sortida is not None:
			a.sortida = a.sortida.isoformat()
    	        alumnesAssistents.append(a)
    return render(request, 'profe/assistenciaclasse.html',
                  {'classe': classe, 'data': data, 'noassistents': not_assistencies,
                   'assistents': alumnesAssistents})
