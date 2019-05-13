from django import forms
from .models import MySampleModel


class SampleModelForm(forms.ModelForm):

    class Meta:
        model = MySampleModel
        fields = ['', '', '']

