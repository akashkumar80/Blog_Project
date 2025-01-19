from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    posted_at=models.DateTimeField(auto_now_add=True)
    blog_post=models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='blog_comment')

