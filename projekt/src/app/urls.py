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
    path('knjiga/<int:pk>/brisi/', views.KnjigaDelete.as_view(), name='knjiga-brisi'),
    path('knjiga/novi', views.KnjigaCreate.as_view(), name='knjiga-novi'),
    path('autori/', views.ListaAutora.as_view(), name='autori'),
    path('autor/<int:pk>',views.AutorOpisView.as_view(), name='autor-opis'),
    path('autor/<int:pk>/brisi/', views.AutorDelete.as_view(), name='autor-brisi'),
    path('autor/novi', views.AutorCreate.as_view(), name='autor-novi'),
    path('zanr/novi', views.ZanrCreate.as_view(), name='zanr-novi'),
    path('knjigai/novi', views.KnjigaIzdanjeCreate.as_view(), name='knjigai-novi'),
    path('zanrovi/', views.ListaZanr.as_view(), name='zanrovi'),
    path('zanr/<int:pk>/brisi/', views.ZanrDelete.as_view(), name='zanr-brisi'),
]