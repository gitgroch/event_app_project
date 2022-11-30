from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm


# Create post list view 
class PostList(generic.ListView):
    model = Post
    # Filter post view to published and order by creation date
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 8


# Post Detail View 
class PostDetail(View):

    def get(self, request, slug,):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug,):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

# Post Like View
class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Post Create View
class PostCreate(View):

    def get(self, request):
        """
        Retrieving the form
        """

        return render(request, "make_post.html", {"post_form": PostForm()})

    def post(self, request):
        """
        Posting the event after form completion
        """

        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post  = post_form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request,
                             'The event has been posted successfully')
            return redirect('my_garage')
        else:
            post_form = PostForm()

            return render(
                request, "make_post.html",
                {
                    "post_form": post_form
                },
            )

    
    # template_name ='make_post.hmtl'
    # form_class = PostForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class

    #     return render(
    #         request,
    #         "make_post.html",
    #         {
    #             "post_form": Postform()
    #         },
    #     )

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResonseRedirect(reverse('list-view'))
    #     else:
    #         return render(request, self.template_name, {'form': form})
        
        