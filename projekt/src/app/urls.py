from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Knjiznica-home'),
    #path('pknjige/', views.pknjige, name='Knjiznica-pknjige'),
   	#path('nknjige/', views.nknjige, name='Knjiznica-neposudjene knjige'),
    path('mknjige/', views.PosudjeneKnjigePoKorisnicima.as_view(), name='moje-knjige'),
    path('knjige/', views.ListaKnjiga.as_view(), name='knjige'),
    path(r'posudjeno/', views.ListaSvihPKnjiga.as_view(), name='posudjeno-sve'),
    path(r'posuditi/', views.ListaSvihNKnjiga.as_view(), name='neposudjeno-sve'),
    path('knjiga/<uuid:pk>/obnovi/', views.obnoviKnjigu.as_view(), name='knjiznicar'),
    path('vrati/<uuid:pk>', views.Vratiview.as_view(), name='vrati'),
    path('posudi/<uuid:pk>', views.Posudiview.as_view(), name='posudi'),
    path('knjiga/<int:pk>', views.KnjigaOpisView.as_view(), name='knjiga-opis'),
    path('autor/<int:pk>',views.AutorOpisView.as_view(), name='autor-opis'),
]