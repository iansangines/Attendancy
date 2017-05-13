


# Create your views here.
import datetime

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
    user = User.objects.create_user(username=request.username, password=request.password, email=request.email,
                                    first_name=request.name, second_name=request.surname)
    insertedUser = user.save()
    alumne = Alumne(user=insertedUser, dni=request.dni)
    alumne.save()
    # fer login
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
@login_required
def altaDispositiu(request):
    user = User.objects.get(id=request.user.id)
    # #comprobar si esta autenticat (que ho estara fijo)
    # authenticatedUser = authenticate(username=user.username, password=user.password)
    alumne = Alumne.objects.get(user=user)
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
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



class Assistencies(APIView):
    def get(self, request,id_classe, mac_dispositiu):
        # print (id_classe)
        return Response(status=status.HTTP_200_OK)

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
        day = datetime.time.strftime("%a")
        print(mac_sala)
        print(dies[day])
        classes = Classe.objects.filter(sala__MAC=mac_sala).filter(dia=dies[day])
        if not classes:
            return Response(status=status.HTTP_404_NOT_FOUND)
        alumnes_classes = []
        for classe in classes:
            classeAlumnes = ClasseAlumne.objects.filter(classe=classe)
            mac_dispositius = []
            for classeAlumnes in classeAlumnes:
                dispositiu_alumne = classeAlumnes.alumne.dispositiu
                if dispositiu_alumne is None:
                    break
                mac_dispositius.append(dispositiu_alumne.MAC)
            alumnes_classe = {'classe': ClasseSerializer(classe).data, 'mac_dispositius': mac_dispositius}
            alumnes_classes.append(alumnes_classe)
        return JsonResponse(alumnes_classes, safe=False)


@api_view(['GET'])
def getCodi(request, mac):
    try:
        print(mac)
        dispositiu = Dispositiu.objects.get(MAC=mac)
    except Dispositiu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({'codi': dispositiu.codi})
