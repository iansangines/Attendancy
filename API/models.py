from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)


class Alumne(UserProfile):
    dni = models.CharField(max_length=8, validators=[RegexValidator(regex=" (([X-Z]{1})([-]?)(\d{7})([-]?)([A-Z]{1}))|((\d{8})([-]?)([A-Z]{1}))", message="El DNI/NIE no es valid")], unique=True)
    dispositiu = models.OneToOneField('Dispositiu', null=True)
    # Com a string perque la classe Dispositiu es creara mes endavant


class Professor(UserProfile):
    classes = models.ManyToManyField('Classe')


class Dispositiu(models.Model):
    MAC = models.CharField(max_length=17, validators=[RegexValidator(regex="^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", message="MAC no valida",  code="invalid_mac")], unique=True)
    codi = models.CharField(max_length=256)


class Sala(models.Model):
    nom = models.CharField(max_length=256)
    MAC = models.CharField(max_length=17,validators=[RegexValidator(regex="^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", message="MAC no valida", code="invalid_mac")], unique=True)
    #Possible forat de seguretat si no es controla que una mac de dispositiu estigui a una mac de sala :)


class Classe(models.Model):
    assignatura = models.CharField(max_length=256)
    professorTutor = models.ForeignKey(Professor)
    sala = models.ForeignKey(Sala)
    dia = models.IntegerField()
    horaInici = models.TimeField()
    horaFinal = models.TimeField()


class ClasseAlumne(models.Model):
    alumne = models.ForeignKey(Alumne)
    classe = models.ForeignKey(Classe)


class Assistencia(models.Model):
    classeAlumne = models.ForeignKey(ClasseAlumne)
    entrada = models.DateTimeField()
    sortida = models.DateTimeField(null=True)
