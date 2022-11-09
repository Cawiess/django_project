from django.shortcuts import render, get_object_or_404

from .models import Post

# Some temporary dummy data for posts

'''
all_posts = [
    {
        "slug": "placeholders-are-great",
        "image": "mountains.jpg",
        "author": "Carl",
        "date": date(2021, 7, 21),
        "title": "Post dummy title one",
        "excerpt": "There's nothing like the placeholders you get when doing Django! I truly enjoy it!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "placeholders-are-fun",
        "image": "coding.jpg",
        "author": "Carl",
        "date": date(2022, 3, 10),
        "title": "Post dummy title two",
        "excerpt": "Did you ever spend a whole night thinking about placeholders? I just love it!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "placeholders-are-healthy",
        "image": "woods.jpg",
        "author": "Carl",
        "date": date(2020, 8, 5),
        "title": "Post dummy title three",
        "excerpt": "Placeholders is amazing! The amount of inspiration I feel from writing them is immense!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

'''

# Create your views here.

def starting_page(request):
    #sorted_posts = sorted(all_posts, key=get_date)
    #latest_posts = sorted_posts[-3:]
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    #identified_post = next(post for post in all_posts if post['slug']==slug)
    identified_post = get_object_or_404(Post, slug=slug) #Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })