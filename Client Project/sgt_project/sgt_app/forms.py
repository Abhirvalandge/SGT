from django import forms
from .models import *
from django.forms.widgets import DateInput

class AddEntryForm(forms.ModelForm):
    class Meta:
        model = SGTEntries
        fields = ['date','firm_name','lr_no','vehicle_no', 'location',
                    'amount', 'cash', 'diesel', 'rtgs', 'commission', 'status']
        widgets = {'date':DateInput(attrs={'type':'date'})}