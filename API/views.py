import time
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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


@api_view(['GET'])
def get_alumnes_classe(request):
    mac = MacSerializer(data=request.data)
    classe = Classe.objects.get(Sala=Sala.objects.get(MAC=mac))
    alumnes_classe = ClasseAlumne.objects.filter(classe=classe)
    return JsonResponse(alumnes_classe)


class getCodi():
    def get(self, request):
        mac = request.mac
        dispositiu = Dispositiu.objects.get(MAC=mac)
        if dispositiu is None:
            return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return JsonResponse({'codi': dispositiu.codi})


class control_assstencia():
    def post(self, request):
        mac = request.mac
        classe = request.classe
        alumne = Dispositiu.objects.get(MAC=mac).alumne
        if alumne is None:
            return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)

        classeAlumne = ClasseAlumne.objects.get(alumne=alumne, classe=classe)
        if classeAlumne is None:
            return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)

        entrada = time.time()
        assistencia = Assistencia(classeAlumne=classealumne, entrada=entrada)
        assistencia.save()
        return HttpResponse(status_code=status.HTTP_201_CREATED)

    def put(self, request, format=None):
        mac = request.mac
        classe = request.classe
        alumne = Dispositiu.objects.get(MAC=mac).alumne
        if alumne is None:
            return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)

        classeAlumne = ClasseAlumne.objects.get(alumne=alumne, classe=classe)
        if classeAlumne is None:
            return HttpResponse(status_code=status.HTTP_404_NOT_FOUND)

        assistencia = Assistencia.objects.filter(classeAlumne=classeAlumne).order_by('-entrada')[0] #Obte la primera entrada mes gran, es a dir, la ultima entrada ue ha tingut aquest alumne
        sortida = time.time()
        assistencia.sortida = sortida
        assistencia.save()
        return HttpResponse(status_code=status.HTTP_200_OK)


class UsersList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserprofilesList(APIView):
    def get(self, request, format=None):
        userprofiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlumnesList(APIView):
    def get(self, request, format=None):
        alumnes = Alumne.objects.all()
        serializer = AlumneSerializer(alumnes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessorsList(APIView):
    def get(self, request, format=None):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DispositiusList(APIView):
    def get(self, request, format=None):
        dispositius = Dispositiu.objects.all()
        serializer = DispositiuSerializer(dispositius, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DispositiuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesList(APIView):
    def get(self, request, format=None):
        sales = Sala.objects.all()
        serializer = SalaSerializer(sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassesList(APIView):
    def get(self, request, format=None):
        classes = Classe.objects.all()
        serializer = ClasseSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClasseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClasseAlumneList(APIView):
    def get(self, request, format=None):
        classealumne = ClasseAlumne.objects.all()
        serializer = ClasseAlumneSerializer(classealumne, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClasseAlumneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClasseProfeList(APIView):
    def get(self, request, format=None):
        classeprofe = ClasseProfe.objects.all()
        serializer = ClasseProfeSerializer(classeprofe, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClasseProfeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssistenciesList(APIView):
    def get(self, request, format=None):
        assistencies = Assistencia.objects.all()
        serializer = AssistenciaSerializer(assistencies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignaturesList(APIView):
    def get(self, request, format=None):
        assignatures = Assignatura.objects.all()
        serializer = AssignaturaSerializer(assignatures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

