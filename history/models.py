from django.db import models
from person.models import Persona

# Create your models here.

class History(models.Model):
	usuario=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	History1 = models.CharField(max_length=100, null=True)
	History2 = models.CharField(max_length=100, null=True)
	History3 = models.CharField(max_length=100, null=True)
	History4 = models.CharField(max_length=100, null=True)
	History5 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='history'
		verbose_name_plural='historys'

	def __str__(self):
		return '{}'.format(self.usuario)