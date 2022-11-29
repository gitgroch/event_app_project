from django.shortcuts import render
from django.views import generic
from .models import Post

# Create post list view 
class PostList(generic.ListView):
    model = Post
    # Filter post view to published and order by creation date
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 10
    



