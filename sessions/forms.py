from django import forms
from django.forms import ModelForm
from .models import Sessions

class SessionsForm(ModelForm):
    class Meta:
        model = Sessions
        fields = ('Name', 'Job_No', 'Vessel', 'Port_Name', 'Equipment', 'Issue_Date')