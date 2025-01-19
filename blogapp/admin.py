from django.contrib import admin
from .models import BlogPost,Comment

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','author','created_at','updated_at')
    search_fields=('title','author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('posted_by','posted_at','comment','blog_post')
