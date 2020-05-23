from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Knjiznica-home'),
    path('about/', views.about, name='Knjiznica-about'),
]