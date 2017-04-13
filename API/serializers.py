from rest_framework import serializers
from models import *
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','user','alumne','professor')

class AlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumne
        fields = ('id','dni', 'dispositiu')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id','classes',)

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
        fields = ('id','professorTutor', 'sala', 'horaInici', 'horaFinal')

class ClasseAlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseAlumne
        fields = ('id','alumne','classe')

class AssistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistencia
        fields = ('id','dispositiuAlumne', 'classeAlumne', 'horaEntrada', 'horaSortida')
