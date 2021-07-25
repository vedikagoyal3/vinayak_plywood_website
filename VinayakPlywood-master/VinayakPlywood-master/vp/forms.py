from django.forms import ModelForm
from django import forms
from vp.models import query
class query_form(forms.ModelForm):
    class Meta:
        model=query
        fields=('name','email','subject','message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder':'Message'}),
        }
