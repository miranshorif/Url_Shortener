from django import forms
from .models import Shortener


class ShortenerForms(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(attrs={'class':'form-conrol form-control-lg','placeholder':'Your url to shortener'}))
    
    class Meta:
        model = Shortener
        
        fields = ['long_url',]