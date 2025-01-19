from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import HttpResponse
from .models import BlogPost,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def home(request):
    blogs=BlogPost.objects.all().order_by('created_at')
    return render(request,'blogapp/home.html',{'blogs':blogs})

def blog_detail(request,pk):
    blog=BlogPost.objects.filter(pk=pk)
    if blog.exists():
        blog=BlogPost.objects.get(pk=pk)
        return render(request,'blogapp/blog_detail.html',{'blog':blog})
    else:
        return HttpResponse("Blog Doesn\'t Exist")
    
@login_required(redirect_field_name='users:login',login_url='users:login')
def blog_create(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        blog=BlogPost(title=title,content=content,author=request.user)
        blog.save()
        return redirect('blog:home')
    else:
        return render(request,'blogapp/create.html')
    

@login_required(redirect_field_name='users:login',login_url='users:login')
def blog_update(request,pk):
    blog=get_object_or_404(BlogPost,pk=pk,author=request.user)
    if request.method=='POST':
        blog.title=request.POST['title']
        blog.content=request.POST['content']
        blog.save()
        messages.success(request,"Blog Updated Successfully")
        return redirect('blog:detail',pk=blog.pk)
    else:
        return render(request,'blogapp/update.html',{'blog':blog})


@login_required(redirect_field_name='users:login',login_url='users:login')
def blog_delete(request,pk):
    blog=get_object_or_404(BlogPost,pk=pk,author=request.user)
    if request.method=='POST':
        blog.delete()
        return redirect('blog:home')
    
@login_required(redirect_field_name='users:login',login_url='users:login')
def my_blog(request,author):
    user=get_object_or_404(User,pk=author)
    blogs=BlogPost.objects.filter(author=user)
    return render(request,'blogapp/my_blogs.html',{'blogs':blogs})



@login_required(redirect_field_name='users:login',login_url='users:login')
def add_comment(request,pk):
    if request.method=="POST":
        blog=get_object_or_404(BlogPost,pk=pk)
        comment=request.POST['comment']
        if comment:
            post_comment=Comment(comment=comment,posted_by=request.user,blog_post=blog)
            post_comment.save()
            messages.success(request,"Comment Added Successfullt")
        return redirect('blog:detail',pk=pk)
    

@login_required(redirect_field_name='users:login',login_url='users:login')
def delete_comment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    if request.user==comment.posted_by:
        comment.delete()
        messages.success(request,"Your Comment was Deleted Successfully")
    else:
        messages.error(request,"Unauthorized Request")
    return redirect('blog:detail',pk=comment.blog_post.id)