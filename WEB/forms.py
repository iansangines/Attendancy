from django import forms

class SalaForm(forms.Form):
    name = forms.CharField(label='nom', max_length=100)
    MAC = forms.CharField(label='MAC', max_length=100)

class ProfessorForm(forms.Form):
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='password', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    email = forms.CharField(label='email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='first name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
