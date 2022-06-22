from django import forms
from django.forms import ModelForm
from .models import Sessions

class SessionsForm(ModelForm):
    class Meta:
        model = Sessions
        fields = ('Name', 'Job_No', 'Vessel', 'Port_Name', 'Equipment', 'Issue_Date')
        labels = {
            'Name': 'Name',
            'Job_No': 'Job Number',
            'Vessel': 'Vessel/Cust',
            'Port_Name': 'Port Name',
            'Equipment': 'Equipment',
            'Issue_Date': 'Issue Date',
        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Vessel': forms.TextInput(attrs={'class': 'form-control'}),
            'Port_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Equipment': forms.TextInput(attrs={'class': 'form-control'}),
            'Issue_Date': forms.TextInput(attrs={'class': 'form-control'})
        }