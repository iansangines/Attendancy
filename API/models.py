from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)


class Alumne(UserProfile):
    dni = models.CharField(max_length=8, unique=True)
    dispositiu = models.OneToOneField('Dispositiu')
    # Com a string perque la classe Dispositiu es creara mes endavant


class Professor(UserProfile):
    classes = models.ManyToManyField('Classe')


class Dispositiu(models.Model):
    MAC = models.CharField(max_length=17, primary_key=True)
    codi = models.CharField(max_length=256)


class Sala(models.Model):
    nom = models.CharField(max_length=256)
    MAC = models.CharField(max_length=17, primary_key=True)


class Classe(models.Model):
    professorTutor = models.ForeignKey(Professor)
    sala = models.ForeignKey(Sala)
    horaInici = models.TimeField()
    horaFinal = models.TimeField()


class ClasseAlumne(models.Model):
    alumne = models.ForeignKey(Alumne)
    classe = models.ForeignKey(Classe)


class Assistencia(models.Model):
    dispositiuAlumne = models.ForeignKey(Dispositiu)
    classeAlumne = models.ForeignKey(Classe)
    horaEntrada = models.TimeField()
    horaSortida = models.TimeField()