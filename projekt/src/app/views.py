from django.shortcuts import render
from .models import Knjiga, KnjigaIzdanje

def home(request):

	br_knjiga = Knjiga.objects.all().count()
	br_izdanja = KnjigaIzdanje.objects.all().count()
	br_izdanja_d = KnjigaIzdanje.objects.filter(status__exact= 'd' ).count()
	br_izdanja_p = KnjigaIzdanje.objects.filter(status__exact= 'p').count()
	context = {
		'br_knjiga': br_knjiga,
		'br_izdanja': br_izdanja,
		'br_izdanja_d': br_izdanja_d,
		'br_izdanja_p': br_izdanja_p,
	}

	return render(request, 'app/home.html', context = context)

def pknjige(request):

	status = KnjigaIzdanje.objects.filter(status__exact= 'p' )
	context = {
	'posts': Knjiga.objects.all(),
	'status': status
	}
	return render(request, 'app/pknjige.html', context)

def nknjige(request):

	status = KnjigaIzdanje.objects.filter(status__exact= 'd' )
	context = {
	'posts': Knjiga.objects.all(),
	'status': status,
	}
	return render (request, 'app/nknjige.html', context)
    
    	
 