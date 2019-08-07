from django import forms
from .models import Editor, Comment

class Editor_create(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ['title','body', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]