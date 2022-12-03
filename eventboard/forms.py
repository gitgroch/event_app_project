from .models import Comment, Post
from django import forms
from crispy_forms.helper import FormHelper


COUNTY_CHOICES = [
                ('1', 'Carlow'), ('2', 'Cavan'), ('3', 'Clare'),
                ('4', 'Cork'), ('5', 'Donegal'), ('6', 'Dublin'),
                ('7', 'Galway'), ('8', 'Kerry'), ('9', 'Kildare'),
                ('10', 'Kilkenny'), ('11', 'Laois'), ('12', 'Leitrim'),
                ('13', 'Limerick'), ('14', 'Longford'), ('15', 'Louth'),
                ('16', 'Mayo'), ('17', 'Meath'), ('18', 'Monaghan'),
                ('19', 'Offaly'), ('20', 'Roscommon'), ('21', 'Sligo'),
                ('22', 'Tipperary'), ('23', 'Waterford'), ('24', 'Westmeath'),
                ('25', 'Wexford'), ('26', 'Wicklow'),
                 ]

CATEGORY_CHOICES = [
                    ('1', 'Sport'), ('2', 'Business'), ('3', 'Family'),
                    ('4', 'Hobby'), ('5', 'Holiday'), ('6', 'Outdoors'),
                    ('7', 'Music'), ('8', 'Festival')
]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    # category = forms.CharField(
    #     label="Choose a Category:",
    #     widget=forms.Select(choices=CATEGORY_CHOICES))
    # county = forms.CharField(
    #     label="Choose a County:",
    #     widget=forms.Select(choices=COUNTY_CHOICES))
    event_date_and_time = forms.DateField(widget=forms.SelectDateWidget(),)

    class Meta:
        model = Post
        fields = ('title', 'event_location', 'excerpt', 'content', 
                  'featured_image', 'event_date_and_time', 'category', 'county',)
