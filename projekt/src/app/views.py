from django.shortcuts import render
from .models import Knjiga

def home(request):
	return render(request, 'app/home.html', {'title': 'Knjiznica-home'})

def pknjige(request):
	context = {
	'posts': Knjiga.objects.all()
	}
	return render(request, 'app/pknjige.html', context)

def nknjige(request):
    context = {
    'posts': Knjiga.objects.all()
    }
    return render(request, 'app/nknjige.html',  context)