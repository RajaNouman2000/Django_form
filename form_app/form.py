from django import forms
from .models import Registeration_form


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Registeration_form
        fields = '__all__'
