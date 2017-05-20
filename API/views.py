


# Create your views here.
import datetime
import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import *
from API.serializers import *


def index(request):
    return HttpResponse("To see models: http://localhost:8000/API/#modelname#")


@api_view(['POST'])
def altaAlumne(request):
    print(request.data)
    serializedUser = UserSerializer(data=request.data)
    if serializedUser.is_valid():
        user = User.objects.create_user(email=serializedUser.validated_data['email'],
            username=serializedUser.validated_data['username'],
            password=serializedUser.validated_data['password'],
            first_name=serializedUser.validated_data['first_name'],
            last_name=serializedUser.validated_data['last_name'])
        user.save()
        alumne = Alumne(user=user, dni=request.data["dni"])
        alumne.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializedUser.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def altaDispositiu(request, username):
    print(request.data)
    print(username)
    try:
        user = User.objects.get(username=username)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error":"There's no user with this username"})
    try:
        alumne = Alumne.objects.get(user=user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "There's no Alumne with this username"})
    if alumne.dispositiu is None:
        dispositiuSerializer = DispositiuSerializer(data=request.data)
        if dispositiuSerializer.is_valid():
            nouDispositiu = dispositiuSerializer.save()
        else:
            return Response(dispositiuSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        alumne.dispositiu = nouDispositiu
        alumne.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        print(alumne.dispositiu.MAC)
        return Response(status=status.HTTP_409_CONFLICT, data={"error":"This Alumne already has a Dispositiu"})

class Assistencies(APIView):
    def get(self, request,id_classe, mac_dispositiu):
        print (id_classe)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request,id_classe, mac_dispositiu):
        print("post assistencia")
        print(request.data["hora_entrada"])
        entrada = request.data["hora_entrada"]
        try:
            classe = Classe.objects.get(id=id_classe)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any Classe with this Id"})
        try:
            alumne = Alumne.objects.get(dispositiu__MAC=mac_dispositiu)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any Alumne with this MAC"})
        try:
            classeAlumne = ClasseAlumne.objects.get(classe=classe, alumne=alumne)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any ClasseAlumne with this Alumne or Classe"})

        try:
            assistencia = Assistencia(classeAlumne=classeAlumne, data=datetime.datetime.now().date(),
                                      entrada=datetime.datetime.strptime(entrada, '%H:%M').time(), sortida=None)
            print(assistencia)
            assistencia.save(True)
        except ValueError:
            print(ValueError)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Can't save Assistencia object"})

        return Response(status=status.HTTP_201_CREATED)


    def put(self, request, id_classe, mac_dispositiu):
        sortida = request.data["hora_sortida"]
        try:
            classe = Classe.objects.get(id=id_classe)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any Classe with this Id"})
        try:
            alumne = Alumne.objects.get(dispositiu__MAC=mac_dispositiu)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any Alumne with this MAC"})
        try:
            classeAlumne = ClasseAlumne.objects.get(classe=classe, alumne=alumne)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any ClasseAlumne with this Alumne or Classe"})
        try:
            assistencia = Assistencia.objects.filter(classeAlumne=classeAlumne).filter(sortida=None).filter(data=datetime.datetime.now().date()).latest('id')
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any Assistencia with this parameters"})
        try:
            assistencia.sortida=sortida
            assistencia.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "Can't save Assistencia object"})
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_alumnesClasse(request):
    mac_sala = request.GET.get('mac')
    dies = {'Mon': 'dilluns', 'Tue': 'dimarts', 'Wed': 'dimecres', 'Thu': 'dijous', 'Fri': 'divendres'}
    if mac_sala is not None:
        day = time.strftime("%a")
        print(mac_sala)
        if day == "Sat" or day == "Sun":
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":"There's no class today, you really wanna work?"})
        classes = Classe.objects.filter(sala__MAC=mac_sala).filter(dia=dies[day])
        if not classes:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Not found any Classe with this MAC"})
        alumnes_classes = []
        for classe in classes:
            classeAlumnes = ClasseAlumne.objects.filter(classe=classe)
            mac_dispositius = []
            for classealumne in classeAlumnes:
                dispositiu_alumne = classealumne.alumne.dispositiu
                if dispositiu_alumne is None:
                    print "L'alumne" + classealumne.alumne.user.username + "no te dispositiu"
                    break
                mac_dispositius.append(dispositiu_alumne.MAC)
            alumnes_classe = {'classe': ClasseSerializer(classe).data, 'mac_dispositius': mac_dispositius}
            alumnes_classes.append(alumnes_classe)
        return JsonResponse(status=status.HTTP_200_OK, data=alumnes_classes, safe=False)


@api_view(['GET'])
def getCodi(request, mac):
    try:
        print(mac)
        dispositiu = Dispositiu.objects.get(MAC=mac)
    except Dispositiu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({'codi': dispositiu.codi})
