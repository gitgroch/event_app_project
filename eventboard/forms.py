from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Post
        fields = ('title', 'author', 'event_location', 'event_date_and_time',
                    'content', 'featured_image', 'created_on', )

        widgets = {
            'overview': SummernoteWidget(),
            'specifications': SummernoteWidget(),
            'plans': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields[
                'event_image'
                ].label = "Upload an image for your event"
        self.fields[
                'overview'
                ].label = "Event Overview"
      
