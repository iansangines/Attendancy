#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import *
from serializers import *

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the API index.")

def classes(request):
    classes = Classe.objects.all()
    serializer = ClasseSerializer(classes, many=True)
    return JsonResponse(serializer.data, safe=False)
    #return HttpResponse("Retorna JSON amb les clases")

