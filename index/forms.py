from django import forms
from index.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nicname', 'content', 'article', 'email']
