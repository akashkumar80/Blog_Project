from django.urls import path
from . import views


app_name="blog"
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:pk>/',views.blog_detail,name='detail'),
    path('create/',views.blog_create,name='create'),
    path('<int:pk>/update',views.blog_update,name='update'),
    path('<int:pk>',views.blog_delete,name='delete'),
    path('<int:author>/blogs',views.my_blog,name='my_blog'),
    path('<int:pk>/add_comment',views.add_comment,name='add_comment'),
    path('<int:pk>/delete_comment',views.delete_comment,name='delete_comment')
]