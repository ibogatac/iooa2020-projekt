from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
# Create your models here.

class Knjiga(models.Model):
	naziv = models.CharField(max_length = 60)
	autor = models.CharField(max_length = 30)
	izdavacka_kuca = models.CharField(max_length = 50)
	godina_izdanja = models.DateField(auto_now_add = False, auto_now = False)

	def __str__(self):
		return self.naziv

 

class KnjigaIzdanje(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unikatan id za knjigu')
    knjiga = models.ForeignKey('Knjiga', on_delete=models.SET_NULL, null=True) 
    izdanje = models.CharField(max_length=200)
    vracanje = models.DateField(null=True, blank=True)
    posudjivac = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)



    STATUS_KNJIGE = (
        
        ('p', 'Posudjena'),
        ('d', 'Dostupna'),
        
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_KNJIGE,
        blank=True,
        default='d',
        
    )
    class Meta:
        ordering = ['vracanje']
        permissions = (('obnova', 'obnoviti'),)
        
    

    @property
    def vratiti(self):

        if self.vracanje and date.today() > self.vracanje:
            return True
        return False


    




