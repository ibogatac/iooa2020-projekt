from django.contrib import admin

# Register your models here.
from .models import Knjiga, KnjigaIzdanje
from .forms import KnjigaForm

class KnjigaAdmin(admin.ModelAdmin):
	list_display = ['naziv', 'autor', 'izdavacka_kuca', 'godina_izdanja',]
	form = KnjigaForm
	list_filter = ['autor']
	search_fields = ['naziv', 'autor', 'izdavacka_kuca']



admin.site.register(Knjiga, KnjigaAdmin)
admin.site.register(KnjigaIzdanje)
