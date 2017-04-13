from rest_framework import serializers
from models import *


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('professorTutor', 'sala', 'horaInici', 'horaFinal')