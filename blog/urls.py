from django.urls import path

from . import views
'''
urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"), #/posts/
    path("posts/<slug>", views.single_post, name="single-post-page") #/posts/post
]
'''



urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page")  # /posts/my-first-post
]