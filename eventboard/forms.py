from .models import Comment
from django import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
