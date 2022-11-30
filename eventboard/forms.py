from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = ('title', 'event_location', 
                    'content', 'featured_image',  )
      
