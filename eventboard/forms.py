from .models import Comment, Post
from django import forms
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    event_date_and_time = forms.DateField(widget=forms.SelectDateWidget(),)

    class Meta:
        model = Post
        fields = ('title', 'event_location', 'category', 'county', 'excerpt',
                  'content', 'featured_image', 'event_date_and_time',
                  'contact_phone', 'contact_email', 'contact_website',
                  'contact_address',
                  )
