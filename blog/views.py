from django.shortcuts import render
from .models import Post



# Create your views here.
def blog(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)




def blog_post(request, post_id):
    post = Post.objects.get(id = post_id)

    context = {
        'post': post,
    }
    
    return render(request, 'blog/blog_post.html', context)