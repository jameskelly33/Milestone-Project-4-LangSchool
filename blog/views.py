from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post



# Create your views here.
def blog(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)



@login_required
def blog_post(request, post_id):
    post = Post.objects.get(id = post_id)
    total_likes = post.total_likes()
    user_liked = False
    if request.user in post.likes.all():
        user_liked=True
        

    context = {
        'post': post,
        'total_likes':total_likes,
        'user_liked':user_liked,
    }
    
    return render(request, 'blog/blog_post.html', context)

def like(request, post_id):
    post = Post.objects.get(id = post_id)     
    post.likes.add(request.user)
    messages.success(request, 'Thanks for liking this post!')
    
   
    context ={
        'post':post

    }
    
    return redirect(reverse('blog_post', args=[str(post_id)]))