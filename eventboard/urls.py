from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:id>/delete-post', views.delete_post, name='delete_post'),
    path('<int:id>/delete-comment', views.delete_comment, name='delete_comment'),
]