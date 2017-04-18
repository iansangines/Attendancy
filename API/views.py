from django.contrib.auth import authenticate
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

class ClassealumneList(APIView):
    
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
#######################################################################################
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
########################################################################################
@api_view(['POST'])
def altaAlumne(request):
    user = User.objects.create_user(username=request.username, password=request.password, email=request.email,
                                    first_name=request.name, second_name=request.surname)
    insertedUser = user.save()
    alumne = Alumne(user=insertedUser, dni=request.dni)
    alumne.save()
    #fer login
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
@login_required
def altaDispositiu(request):
    user = User.objects.get(id=request.user.id)
    #comprobar si esta autenticat (que ho estara fijo)
    authenticatedUser = authenticate(username=user.username, password=user.password)
    alumne = Alumne.objects.get(user=user)
    if alumne.dispositiu is None:
        dispositiuSerializer = DispositiuSerializer(data=request.data)
        if dispositiuSerializer.is_valid():
            nouDispositiu = dispositiuSerializer.save()
        else:
            return Response(dispositiuSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        alumne.dispositiu = nouDispositiu
        alumne.save()
        return Response(dispositiuSerializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)

