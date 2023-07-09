from django.views.generic import CreateView
from english.models import English
from english.forms import RegistroFormEnglish
from django.urls import reverse_lazy

class RegistroEnglish(CreateView):
	model = English
	template_name = "english/new-english.html"
	form_class = RegistroFormEnglish
	success_url = reverse_lazy('history')