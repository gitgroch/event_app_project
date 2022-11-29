from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS - ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")
    updated_on = models.DateTimeField(auto_now=True)
    event_location = models.TextField()
    event_date_and_time = models.DateTimeField()
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField()
    status =  models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name'even_likes', blank=True)