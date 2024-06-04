from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'posts/posts_list.html', {})

def new_post(request):
    return render(request, 'posts/new_post.html', {})