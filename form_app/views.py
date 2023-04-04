from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from . models import Registeration_form
from .form import ApplicationForm


# Create your views here.


def form_view(request):
    form = ApplicationForm()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            uc = Registeration_form(
                # first_name,last_name,comment
                name=cd['name'],
                address=cd['address'],
                field=cd['field'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })

    return render(request, 'form.html', {'form': form})
