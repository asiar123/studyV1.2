from django.views.generic import CreateView
from history.models import History
from history.forms import RegistroFormHistory
from django.urls import reverse_lazy

# Create your views here.

class añadirHistory(CreateView):
	model = History
	template_name = 'history/new-history.html'
	form_class = RegistroFormHistory
	success_url = reverse_lazy('home')