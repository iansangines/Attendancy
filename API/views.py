import time
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from serializers import *


# Create your views here.

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


# class getCodi():
#     def get(self, request):
#         mac_dispositiu = request.GET.get('mac')
#         dispositiu = Dispositiu.objects.get(MAC=mac_dispositiu)
#         if dispositiu is None:
#             return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)
#         else:
#             return JsonResponse({'codi': dispositiu.codi})
#
#
# class control_assstencia():
#     def post(self, request):
#         mac = request.mac
#         classe = request.classe
#         alumne = Dispositiu.objects.get(MAC=mac).alumne
#         if alumne is None:
#             return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)
#
#         classeAlumne = ClasseAlumne.objects.get(alumne=alumne, classe=classe)
#         if classeAlumne is None:
#             return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)
#
#         entrada = time.time()
#         assistencia = Assistencia(classeAlumne=classeAlumne, entrada=entrada)
#         assistencia.save()
#         return HttpResponse(status_code=status.HTTP_201_CREATED)
#
#     def put(self, request, format=None):
#         mac = request.mac
#         classe = request.classe
#         alumne = Dispositiu.objects.get(MAC=mac).alumne
#         if alumne is None:
#             return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)
#
#         classeAlumne = ClasseAlumne.objects.get(alumne=alumne, classe=classe)
#         if classeAlumne is None:
#             return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)
#
#         assistencia = Assistencia.objects.filter(classeAlumne=classeAlumne).order_by('-entrada')[0]  # Obte la primera entrada mes gran, es a dir, la ultima entrada ue ha tingut aquest alumne
#         sortida = time.time()
#         assistencia.sortida = sortida
#         assistencia.save()
#         return HttpResponse(status_code=status.HTTP_200_OK)



def get_alumnesClasse(request):
    mac_sala = request.GET.get('mac')
    dies = {'Mon': 'dilluns', 'Tue': 'dimarts', 'Wed': 'dimecres', 'Thu': 'dijous', 'Fri': 'divendres'}
    if mac_sala is not None:
        day = time.strftime("%a")
        classes = Classe.objects.filter(sala__MAC=mac_sala).filter(dia=dies[day])
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
