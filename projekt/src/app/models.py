from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date, datetime
from django.urls import reverse
# Create your models here.

class Zanr(models.Model):
    naziv = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Žanrovi"

    def __str__(self):
        return self.naziv


class Autor(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    god_rodjenja = models.DateField('Godina rođenja',null=True, blank=True)
    god_smrti = models.DateField('Godina smrti', null=True, blank=True)

    class Meta:
        ordering = ['prezime', 'ime']
        verbose_name_plural = "Autori"

    def get_absolute_url(self):
        return reverse('autor-opis', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.prezime, self.ime)


class Knjiga(models.Model):
    
    naziv = models.CharField(max_length = 60)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    zanr = models.ManyToManyField(Zanr, verbose_name = 'Žanr')
    izdavacka_kuca = models.CharField(max_length = 50)
    godina_izdanja = models.DateField(auto_now_add = False, auto_now = False)

    class Meta:
        verbose_name_plural = "Knjige"

    
    def __str__(self):
        return self.naziv
    def display_zanr(self):
        return ', '.join([zanr.naziv for zanr in self.zanr.all()[:3]])
        display_genre.short_description = 'Žanr'

    def get_absolute_url(self):
        return reverse('knjiga-opis', args=[str(self.id)])

    



 

class KnjigaIzdanje(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unikatan id za knjigu')
    knjiga = models.ForeignKey('Knjiga', on_delete=models.CASCADE, null=True) 
    izdanje = models.CharField(max_length=200)
    vracanje = models.DateField(null=True, blank=True)
    posudjivac = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name = 'Posuđivač')



    STATUS_KNJIGE = (
        
        ('p', 'Posuđena'),
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
        verbose_name_plural = "Izdanja knjiga"
        permissions = (('obnova', 'obnoviti'),)
        
    

    @property
    def vratiti(self):

        if self.vracanje and date.today() > self.vracanje:
            return True
        return False


    def cijena(self):


        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(datetime.now().date()), date_format)
        b = datetime.strptime(str(self.vracanje), date_format)
        delta = a-b
        if delta.days > 0:
            delta_a= delta * 5
            return delta_a.days
        else:
            delta_a = 0
            return delta_a



    




