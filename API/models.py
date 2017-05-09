from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, validate_comma_separated_integer_list
from django.utils.translation import ugettext_lazy as _

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
    algo = models.CharField(max_length=1)


class Dispositiu(models.Model):
    MAC = models.CharField(max_length=17, validators=[RegexValidator(regex="^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", message="MAC no valida",  code="invalid_mac")], unique=True)
    codi = models.CharField(max_length=256)


class Sala(models.Model):
    nom = models.CharField(max_length=256)
    MAC = models.CharField(max_length=17, validators=[RegexValidator(regex="^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", message="MAC no valida", code="invalid_mac")], unique=True)
    #Possible forat de seguretat si no es controla que una mac de dispositiu estigui a una mac de sala :)

    def __unicode__(self):
        return self.nom

class Classe(models.Model):
    DIES_CHOICE = (
        ('dilluns', _('Dilluns')),
        ('dimarts', _('Dimarts')),
        ('dimecres', _('Dimecres')),
        ('dijous', _('Dijous')),
        ('divendres', _('Divendres')),
    )
    assignatura = models.ForeignKey('Assignatura')
    sala = models.ForeignKey(Sala)
    dia = models.CharField(max_length=10,choices=DIES_CHOICE,blank=True)
    horaInici = models.TimeField()
    horaFinal = models.TimeField()

class ClasseProfe(models.Model):
    classe = models.ForeignKey(Classe)
    professor = models.ForeignKey(Professor)

class ClasseAlumne(models.Model):
    alumne = models.ForeignKey(Alumne)
    classe = models.ForeignKey(Classe)


class Assistencia(models.Model):
    classeAlumne = models.ForeignKey(ClasseAlumne)
    entrada = models.DateTimeField()
    sortida = models.DateTimeField(null=True)

class Assignatura(models.Model):
    nom = models.CharField(max_length=256)
    inici = models.DateField()
    final = models.DateField()

    def __unicode__(self):
        return self.nom
