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


class ObnoviForm(forms.Form):
    obnovi_datum = forms.DateField(
            help_text="Unesti datum između sada i 4 tjedna")


    def clean_obnova_datum(self):
        data = self.cleaned_data['obnovi_datum']

        if data < datetime.date.today():
            raise ValidationError(_('Nevažeći datum - datum u prošlosti'))
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Nevažeći datum - datum više od 4 tjedna ispred'))
        return data


class KnjigaIzdanjeForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['status', 'vracanje']


class KnjigaIzdanjePForm(forms.ModelForm):
    class Meta:
        model = KnjigaIzdanje
        fields = ['status', 'vracanje']








