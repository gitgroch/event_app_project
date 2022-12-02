from .models import Comment, Post
from django import forms


COUNTY_CHOICES = [
                ('1', 'Dublin'), 
                ('2', 'Wexford'),
                ]

CATEGORY_CHOICES = [ 
                    ('1', 'Sport' ),
                    ('2', 'Business'),
]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    category = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES))
    
    county = forms.CharField(widget=forms.Select(choices=COUNTY_CHOICES))
    
    event_date_and_time = forms.DateField(widget=forms.SelectDateWidget(),)
    class Meta:
        model = Post
        fields = ('title', 'event_location', 'content','featured_image', 'event_date_and_time' )
