from django.shortcuts import render, redirect
from .models import Knjiga, KnjigaIzdanje, Autor, Zanr
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import permission_required
from .forms import ObnoviForm
from .forms import KnjigaIzdanjeForm
from .forms import KnjigaIzdanjePForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@login_required
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

	return render(request, 'app/home.html', context)
class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'app/home.html'

#def pknjige(request):

	#status = KnjigaIzdanje.objects.filter(status__exact= 'p' )
	#context = {
	#'posts': Knjiga.objects.all(),
	#'status': status
	#}
	#return render(request, 'app/pknjige.html', context)

#def nknjige(request):

	#status = KnjigaIzdanje.objects.filter(status__exact= 'd' )
	#context = {
	#'posts': Knjiga.objects.all(),
	#'status': status,
	#}
	#return render (request, 'app/nknjige.html', context)
    

class PosudjeneKnjigePoKorisnicima(LoginRequiredMixin, generic.ListView):
    model = KnjigaIzdanje
    template_name ='app/pknjigekorisnik.html'
    paginate_by = 10
    
    def get_queryset(self):
        return KnjigaIzdanje.objects.filter(posudjivac=self.request.user).filter(status__exact='p').order_by('vracanje')


class ListaKnjiga(LoginRequiredMixin,generic.ListView):
    model = Knjiga
    paginate_by = 10


class ListaSvihPKnjiga(PermissionRequiredMixin, generic.ListView):
    model = KnjigaIzdanje
    permission_required = 'app.obnova'
    template_name = 'app/listasve.html'
    paginate_by = 10

    def get_queryset(self):
        return KnjigaIzdanje.objects.filter(status__exact='p').order_by('vracanje')

class ListaSvihNKnjiga(PermissionRequiredMixin, generic.ListView):
    model = KnjigaIzdanje
    permission_required = 'app.obnova'
    template_name = 'app/listasven.html'
    paginate_by = 10

    def get_queryset(self):
        return KnjigaIzdanje.objects.filter(status__exact='d')






class obnoviKnjigu(PermissionRequiredMixin, UpdateView):

   
    model = KnjigaIzdanje
    form_class = ObnoviForm
    permission_required = 'app.obnova'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(KnjigaIzdanje, pk=pk_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/posudjeno'





class Vratiview(PermissionRequiredMixin, UpdateView):

   
    model = KnjigaIzdanje
    form_class = KnjigaIzdanjeForm
    permission_required = 'app.obnova'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(KnjigaIzdanje, pk=pk_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/posudjeno'


class Posudiview(PermissionRequiredMixin, UpdateView):

   
    model = KnjigaIzdanje
    form_class = KnjigaIzdanjePForm
    permission_required = 'app.obnova'

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(KnjigaIzdanje, pk=pk_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/posuditi'

class KnjigaOpisView(generic.DetailView):
    model = Knjiga
    
class AutorOpisView(generic.DetailView):
    model = Autor


    

    
 