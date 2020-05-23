from django.db import models

# Create your models here.

class Knjiga(models.Model):
	naziv = models.CharField(max_length = 60)
	autor = models.CharField(max_length = 30)
	izdavacka_kuca = models.CharField(max_length = 50)
	godina_izdanja = models.DateField(auto_now_add = False, auto_now = False)
	status = models.IntegerField()

	def __str__(self):
		return self.naziv



