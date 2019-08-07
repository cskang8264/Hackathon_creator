from django import forms
from .models import Prop, Comment

class Prop_create(forms.ModelForm):
    class Meta:
        model = Prop
        fields = ['title','body', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]