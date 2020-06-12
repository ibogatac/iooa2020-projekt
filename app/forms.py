from django import forms
from .models import Knjiga, KnjigaIzdanje, Autor, Zanr
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            'username': None,
            'email': None,
        }

class KnjigaForm(forms.ModelForm):
    class Meta:
        model = Knjiga
        fields = ['naziv', 'autor', 'zanr','izdavacka_kuca', 'godina_izdanja']
    godina_izdanja = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
        label= 'Godina izdanja'
        )
    
    izdavacka_kuca = forms.CharField(label= 'Izdavačka kuća')


class ObnoviForm(forms.ModelForm):

    class Meta:
        model = KnjigaIzdanje
        fields = ['vracanje']
    vracanje = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
        label = 'Vraćanje'
        )

class KnjigaIzdanjeForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['status','posudjivac','vracanje']
    vracanje = forms.DateField(
        required = False,
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
        label = 'Vraćanje'
        )


class KnjigaIzdanjePForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['status', 'posudjivac', 'vracanje']
    vracanje = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
        label = 'Vraćanje'
        )

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['ime', 'prezime', 'god_rodjenja', 'god_smrti']
        
    god_rodjenja = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
        label= 'Godina rođenja'
        )
    god_smrti = forms.DateField(
        required = False,
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
        label= 'Godina smrti'
        )

class ZanrForm(forms.ModelForm):
    class Meta:
        model = Zanr
        fields = ['naziv']

class KnjigaIzdanjeKForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['knjiga', 'izdanje']

    









