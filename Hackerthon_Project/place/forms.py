from django import forms
from .models import Place

class Place_create(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title','body', 'image']