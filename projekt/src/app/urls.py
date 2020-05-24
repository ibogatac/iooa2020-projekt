from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Knjiznica-home'),
    path('pknjige/', views.pknjige, name='Knjiznica-pknjige'),
    path('nknjige/', views.nknjige, name='Knjiznica-neposudjene knjige'),
]