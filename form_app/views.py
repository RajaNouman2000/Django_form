from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Registeration_form
from .form import ApplicationForm

# Create your views here.


class Home(View):
    def get(self, request):
        form = ApplicationForm()
        return render(request, 'form.html', {'form': form})
