from django.db import models
from person.models import Persona

# Create your models here.

class English(models.Model):
	usuario=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	English1 = models.CharField(max_length=100, null=True)
	English2 = models.CharField(max_length=100, null=True)
	English3 = models.CharField(max_length=100, null=True)
	English4 = models.CharField(max_length=100, null=True)
	English5 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='ingles'
		verbose_name_plural='ingless'

	def __str__(self):
		return '{}'.format(self.usuario)