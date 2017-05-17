from django import forms
from API.models import *
from django.utils.translation import ugettext_lazy as _


class SalaForm(forms.Form):
    name = forms.CharField(label='nom', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    MAC = forms.CharField(label='MAC', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XX:XX:XX:XX:XX'}))


class ProfessorForm(forms.Form):
    username = forms.CharField(label='username', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='password', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    email = forms.CharField(label='email', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='first name', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(label='last name', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))


class assistenciaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('classesProfessor')
        super(assistenciaForm, self).__init__(*args, **kwargs)

        # self.fields['assignaturesProfessor'].queryset = assignatures
        self.fields['assignaturesProfessor'] = forms.ModelChoiceField(queryset=self.choices, initial=0, required=True,
                                                                      to_field_name="assignatura",
                                                                      widget=forms.Select(
                                                                          attrs={'class': 'form-control'}))

    # assignaturesProfessor = forms.ModelChoiceField(initial=0, required=True, to_field_name="assignatura")
    diaClasse = forms.TimeField(widget=forms.TextInput(
        attrs={'id': 'datepicker', 'class': 'form-control', 'placeholder': 'Dia de classe'})
    )


class ClasseForm(forms.Form):

    DIES_CHOICE = (
        ('dilluns', _('Dilluns')),
        ('dimarts', _('Dimarts')),
        ('dimecres', _('Dimecres')),
        ('dijous', _('Dijous')),
        ('divendres', _('Divendres')),
    )
    #assignatura = forms.ModelChoiceField(queryset=Assignatura.objects.all(),
    #                                         widget=forms.Select(attrs={'class': 'form-control'}))
    nom = forms.CharField(label='nom', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    inici = forms.DateField(label='inici',widget=forms.TextInput(attrs={'id': 'datepicker1','class': 'form-control'}))
    final = forms.DateField(label='final',widget=forms.TextInput(attrs={'id': 'datepicker2','class': 'form-control'}))
    sala = forms.ModelChoiceField(queryset=Sala.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    professor = forms.ModelChoiceField(queryset=Professor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))



