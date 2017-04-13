from rest_framework import serializers
from models import *

class AlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumne
        fields = ('dni', 'dispositiu')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('classes')

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
        fields = ('professorTutor', 'sala', 'horaInici', 'horaFinal')

class ClasseAlumneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseAlumne
        fields = ('alumne','clase')

class AssistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistencia
        fields = ('dispositiuAlumne', 'claseAlumne', 'horaEntrada', 'horaSortida')
