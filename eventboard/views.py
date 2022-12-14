from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
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

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1,)
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

    def post(self, request, slug,  *args, **kwargs):

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


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = 'created_on'
            post.status = 1
            post.slug = slugify('-'.join([str(post.author),
                                str(post.title),]),)
            post.save()
            # return HttpResponseRedirect(reverse('home'))
            return render(request, 'post_submit_confirm.html',)
    else:
        form = PostForm()
    return render(request, 'make_post.html', {'form': form})

# Edit Post View


def post_edit(request, slug, ):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = 'created_on'
            post.status = 1
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


@login_required
def delete_post(request, id):
    post = Post.objects.filter(id=id)
    post.delete()
    return redirect('/')


def delete_comment(request, id):
    comment = Comment.objects.filter(id=id)
    comment.delete()
    return redirect('/')

def post_rules(request):
    return render(request, 'post_rules.html')