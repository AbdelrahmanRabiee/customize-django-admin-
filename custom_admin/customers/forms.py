from django import forms
from . import models

class CustomerForm(forms.ModelForm):
    test = forms.CharField()
    class Meta:
        fields = ('email', 'name', 'street_1', 'street_2', 'city', 'state', 'country', 'postal_code', 'test')
        model  = models.Customer