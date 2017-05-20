from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','email','first_name', 'last_name')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','alumne','professor')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id','user','uni',)

class AlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumne
        fields = ('id','user','dni', 'dispositiu')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id','user','uni',)

class DispositiuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositiu
        fields = ('MAC','codi')

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ('nom','MAC')

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('id','assignatura', 'sala', 'dia', 'horaInici', 'horaFinal')

class ClasseAlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseAlumne
        fields = ('alumne','classe')

class ClasseProfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseProfe
        fields = ('professor','classe')

class AssistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistencia
        fields = ('classeAlumne', 'entrada', 'sortida')

class AssignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignatura
        fields = ('codiassig','nom','inici','final')
