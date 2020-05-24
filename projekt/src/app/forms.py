from django import forms
from .models import Knjiga, KnjigaIzdanje

class KnjigaForm(forms.ModelForm):

	class Meta:
		model = Knjiga
		fields = ['naziv', 'autor', 'izdavacka_kuca', 'godina_izdanja']


