from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms import ModelForm
from random import randrange
from constants import *


class DenunciaForm(forms.Form):
  Nombre = forms.CharField(max_length=50,
    help_text='Ingrese un nombre que no contenga espacios.', 
    initial="Juan"+str(randrange(500)))
  Apellido = forms.CharField(max_length=50,
    help_text='Ingrese un apellido que no contenga espacios.', 
    initial="Villalba"+str(randrange(500)))
  DNI = forms.CharField(initial="38000000")
  Telefono = forms.CharField(max_length=50,
    initial="tel"+str(randrange(500)))
  Email = forms.EmailField(max_length=50,
    help_text='Ingrese un Email valido.', 
    initial="juan@asd.com")
  Denunciado = forms.CharField(initial="Pablo Perez")
  Rubro = forms.ChoiceField(choices=BLANK_CHOICE_DASH+list(RUBROS))
  Direccion = forms.CharField(initial="Calle 1234")
  Provincia = forms.ChoiceField(choices=PROVINCIAS)
  Ciudad = forms.ChoiceField(choices=BLANK_CHOICE_DASH+list(CIUDADES))
  Descripcion = forms.CharField(widget=forms.Textarea(
    attrs={'rows':7}),
    initial="Lo vi fumando en la vereda")

  Imagen = forms.ImageField(required=False)


class ContactoForm(forms.Form):
  Nombre = forms.CharField(max_length=50, required=False)
  Email = forms.EmailField(max_length=50, required=False)
  Asunto = forms.CharField(max_length=50, required=False)
  Comentario = forms.CharField(
    widget=forms.Textarea(attrs={'rows':5, 'cols':25}))