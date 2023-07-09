from django.views.generic import CreateView
from matematicas.models import Math
from matematicas.forms import FormMath
from django.urls import reverse_lazy

# Create your views here.

class añadirMath(CreateView):
	model = Math
	form_class = FormMath
	template_name = 'math/new-math.html'
	success_url = reverse_lazy('biology')