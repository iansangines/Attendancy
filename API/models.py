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
    dni = models.TextField(blank=False)
    dispositiu = models.OneToOneField('Dispositiu')


class Professor(UserProfile):
    something = models.TextField()


class Dispositiu(models.Model):
    MAC = models.TextField(blank=False)
    codi = models.TextField(blank=False)


class Sala(models.Model):
    MAC = models.TextField(blank=False)


class Classe(models.Model):
    # hora_inici : models.TimeField
    primo = models.CharField(max_length=100)
