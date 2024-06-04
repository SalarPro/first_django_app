from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {
        "posts": posts
    })

def new_post(request):
    return render(request, 'posts/new_post.html', {})


# post_detail
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {
        "post": post
    })