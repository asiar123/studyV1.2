from django import forms

from english.models import English

from django.contrib.admin.widgets import AutocompleteSelect

class RegistroFormEnglish(forms.ModelForm):

	class Meta:
		model = English

		fields = [
			'usuario',
			'English1',
			'English2',
			'English3',
			'English4',
			'English5',
			
		]
		labels = {
			'usuario': forms.Select(attrs={'class':'form-control'}),
			'English1': '¿Significado de masa?',
			'English2': '¿Que es volúmen?',
			'English3': 'Estado solido',
			'English4': 'Estado gas',
			'English5': 'Estado liquido',
			
		}
		widgets = {
			'English1': forms.TextInput(attrs={'class':'form-control'}),
			'English2': forms.TextInput(attrs={'class':'form-control'}),
			'English3': forms.TextInput(attrs={'class':'form-control'}),
			'English4': forms.TextInput(attrs={'class':'form-control'}),
			'English5': forms.TextInput(attrs={'class':'form-control'}),
		}