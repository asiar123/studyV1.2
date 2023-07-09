from django import forms

from history.models import History

class RegistroFormHistory(forms.ModelForm):

	class Meta:
		model = History

		fields = [
			'usuario',
			'History1',
			'History2',
			'History3',
			'History4',
			'History5',
			
		]
		labels = {
			'usuario': forms.Select(attrs={'class':'form-control'}),
			'History1': '¿Como esta conformada la rama legislitiva de Colombia?',
			'History2': 'La tierra esta constituida por 3 elementos: ¿Cuales son?',
			'History3': 'La historia de la humanidad se compone en la prehistoria (ágrafo) e historia (4000 a.c)',
			'History4': 'Las etapas de la prehistoria son: Edad de piedra y edad de los metales',
			'History5': 'La historia se divide en edad antigua (50000 a.c), edad media(1492-XV), edad moderna(XV-17889)',
			
		}
		widgets = {
			'History1': forms.TextInput(attrs={'class':'form-control'}),
			'History2': forms.TextInput(attrs={'class':'form-control'}),
			'History3': forms.TextInput(attrs={'class':'form-control'}),
			'History4': forms.TextInput(attrs={'class':'form-control'}),
			'History5': forms.TextInput(attrs={'class':'form-control'}),
		}