from django import forms
from .models import Knjiga, KnjigaIzdanje
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 
from django import forms

class KnjigaForm(forms.ModelForm):

	class Meta:
		model = Knjiga
		fields = ['naziv', 'autor', 'izdavacka_kuca', 'godina_izdanja']


class ObnoviForm(forms.ModelForm):

    class Meta:
        model = KnjigaIzdanje
        fields = ['vracanje']
    vracanje = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', )
        )

class KnjigaIzdanjeForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['status','posudjivac','vracanje']
    vracanje = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', )
        )


class KnjigaIzdanjePForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['status', 'posudjivac', 'vracanje']
    vracanje = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', )
        )








