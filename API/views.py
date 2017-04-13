from django.http import HttpResponse, JsonResponse
from models import *
from serializers import *

# Create your views here.

def index(request):
    return HttpResponse("To see models: http://localhost:8000/API/#modelname#")

def userprofiles(request):
    userprofiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(userprofiles, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def alumnes(request):
    alumnes = Alumne.objects.all()
    serializer = AlumneSerializer(alumnes, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def professors(request):
    professors = Professor.objects.all()
    serializer = ProfessorSerializer(professors, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def dispositius(request):
    dispositius = Dispositiu.objects.all()
    serializer = DispositiuSerializer(dispositius, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def sales(request):
    sales = Sala.objects.all()
    serializer = SalaSerializer(sales, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def classes(request):
    classes = Classe.objects.all()
    serializer = ClasseSerializer(classes, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def classealumne(request):
    classealumne = ClasseAlumne.objects.all()
    serializer = ClasseAlumneSerializer(classealumne, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def assistencies(request):
    assistencies = Assistencia.objects.all()
    serializer = AssistenciaSerializer(assistencies, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")



