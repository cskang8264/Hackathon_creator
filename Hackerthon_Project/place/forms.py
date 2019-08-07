from django import forms
from .models import Place, Comment

class Place_create(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title','body', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]