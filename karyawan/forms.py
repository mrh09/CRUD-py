from django.forms import ModelForm
from django import forms
from karyawan.models import Employee

class FormEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput({'class':'form-control'}),
            'position' : forms.TextInput({'class':'form-control'}),
            'division' : forms.TextInput({'class':'form-control'}),
        }