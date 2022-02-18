from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import BlogForm



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


@login_required
def add_post(request):

    """ Add a post to the blog"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = BlogForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new post')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add new post. Please ensure the form is valid.')    
    else:    
        form = BlogForm()
    
    template = 'blog/add_post.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)    

@login_required

def edit_post(request,post_id):
    """ Edit blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
    post = Post.objects.get(pk = post_id) 
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post.')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f"You are editing '{post.title}'")

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a post  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
    post = get_object_or_404(Post, id = post_id)
    post.delete()
    messages.success(request, 'Post deleted.')
    return redirect(reverse('blog'))