from django.db import models
from person.models import Persona

# Create your models here.

class Math(models.Model):
	usuario=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	Matematicas1 = models.CharField(max_length=100, null=True)
	Matematicas2 = models.CharField(max_length=100, null=True)
	Matematicas3 = models.CharField(max_length=100, null=True)
	Matematicas4 = models.CharField(max_length=100, null=True)
	Matematicas5 = models.CharField(max_length=100, null=True)
	Matematicas6 = models.CharField(max_length=100, null=True)
	Matematicas7 = models.CharField(max_length=100, null=True)
	Matematicas8 = models.CharField(max_length=100, null=True)
	Matematicas9 = models.CharField(max_length=100, null=True)
	Matematicas10 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='materia'
		verbose_name_plural='materias'

	def __str__(self):
		return '{}'.format(self.usuario)