from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')
