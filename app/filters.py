import django_filters
from .models import *

class KnjigaFilter(django_filters.FilterSet):
	
	class Meta:
		model = Knjiga
		fields =  {
		'naziv':['icontains'],
		'autor':['exact'],
		}


