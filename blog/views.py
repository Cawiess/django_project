from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post

# Some temporary dummy data for posts

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]

        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordring = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()

        return context


'''
def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug) #Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
'''