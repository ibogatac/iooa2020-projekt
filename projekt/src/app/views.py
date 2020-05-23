from django.shortcuts import render
from .models import Knjiga



def home(request):
	context = {
	'posts': Knjiga.objects.all()

	}
	return render(request, 'app/home.html', context)

def about(request):
    context = {
    'posts': Knjiga.objects.all()
    }
    return render(request, 'app/about.html', context)