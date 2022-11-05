from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"), #/posts/
    path("/posts/<slug>", views.single_post, name="single-post-page") #/posts/post
]