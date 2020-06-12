from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.
from .models import Knjiga, KnjigaIzdanje, Autor, Zanr
from .forms import KnjigaForm


class KnjigaAdmin(admin.ModelAdmin):
	list_display = ['naziv', 'autor', 'izdavacka_kuca', 'godina_izdanja']
	#form = KnjigaForm
	list_filter = ['autor']
	search_fields = ['naziv', 'autor', 'izdavacka_kuca']

class KnjigaIzdanjeAdmin(admin.ModelAdmin):
	
	list_display = ['id','Naziv','status','vracanje', 'posudjivac']

	def Naziv(self, obj):
		return obj.knjiga.naziv
	Naziv.admin_order_field = 'id'
	Naziv.short_description = 'Naziv Knjige'





class AutorAdmin(admin.ModelAdmin):

    list_display = ('prezime',
                    'ime', 'god_rodjenja', 'god_smrti')
    fields = ['prezime', 'ime', 'god_rodjenja', 'god_smrti']
    


	
		



admin.site.register(Knjiga, KnjigaAdmin)
admin.site.register(KnjigaIzdanje, KnjigaIzdanjeAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Zanr)


