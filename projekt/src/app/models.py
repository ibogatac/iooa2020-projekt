from django.db import models
import uuid

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

    STATUS_KNJIGE = (
        ('u', 'U pripravnosti'),
        ('p', 'Posudjena'),
        ('d', 'Dostupna'),
        ('r', 'Rezervirana'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_KNJIGE,
        blank=True,
        default='u',
        help_text='Dostupnost knjige',
    )

    class Meta:
        ordering = ['vracanje']

    def __str__(self):
        return f'{self.id} ({self.knjiga.naziv})'


