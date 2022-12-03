from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

COUNTY_CHOICES = [
                ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'),
                ('Cork', 'Cork'), ('Donegal', 'Donegal'), ('Dublin', 'Dublin'),
                ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'),
                ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'),
                ('Limerick', 'Limerick'), ('Longford', 'Longford'), ('Louth', 'Louth'),
                ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'),
                ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'),
                ('Tipperary', 'Tipperary'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'),
                ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow'),
                 ]

CATEGORY_CHOICES = [
                    ('Sport', 'Sport'), ('Business', 'Business'), ('Family', 'Family'),
                    ('Hobby', 'Hobby'), ('Holiday', 'Holiday'), ('Outdoors', 'Outdoors'),
                    ('Music', 'Music'), ('Festival', 'Festival'), ('Culture', 'Culture')
]


# Create Post Table


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="event_posts")
    updated_on = models.DateTimeField(auto_now=True)
    event_location = models.TextField(max_length=200)
    event_date_and_time = models.DateField(null=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='event_likes',
                                   blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, blank=True)
    county = models.CharField(max_length=200, choices=COUNTY_CHOICES, blank=True)
    contact_phone = models.CharField(max_length=12,blank=True)
    contact_email = models.EmailField(max_length=254, blank=True)
    contact_website = models.CharField(max_length=200,blank=True)
    contact_address = models.TextField(max_length=500,blank=True)

    # Add methods to model
    class Meta:
        # order posts by date created
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    # return number of likes on post
    def number_of_likes(self):
        return self.likes.count()

# Create Comment Table


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
