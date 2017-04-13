#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from models import *
from serializers import *

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the API index.")


class Alumnes(APIView):

    def get(self, request, format=None):
        alumnes = Alumne.objects.all()
        serializer = AlumneSerializer(alumnes, many=True)
        return JsonResponse(serializer.data, safe=False)


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


class SalesList(APIView):
    def get(self, request, format=None):
        salas = Sala.objects.all()
        serializer = SalaSerializer(salas, many=True)
        return Response(serializer.data)



def salas(request):
    salas = Sala.objects.all()
    serializer = SalaSerializer(salas, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def classes(request):
    classes = Classe.objects.all()
    serializer = ClasseSerializer(classes, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def classesalumnes(request):
    classesalumnes = ClasseAlumne.objects.all()
    serializer = ClasseAlumneSerializer(classesalumnes, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

def assistencies(request):
    assistencies = Assistencia.objects.all()
    serializer = AssistenciaSerializer(assistencies, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")



