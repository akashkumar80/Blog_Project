from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('users:login')

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        if User.objects.filter(username=username).exists()==False:
            return render(request,'users/login.html',{'message':'User Doesn\' exist'})
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user)
            return redirect('blog:home')
        else:
            return render(request,'users/login.html',{'message':'Wrong Password'})
    else:
        return render(request,'users/login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        repassword=request.POST['reenterpassword']
        email=request.POST['email']
        
        if password!=repassword:
            return render(request,'users/register.html',{'password_error':"Password is different"})
        if User.objects.filter(username=username).exists():
            return render(request,'users/register.html',{'username_error':"Username Already Exist"})
        if User.objects.filter(email=email).exists():
            return render(request,'users/register.html',{'email_error':"Email Already Exist"})
        
        user=User.objects.create_user(username,email,password)
        user.save()
        return redirect('users:login')
    else:
        return render(request,'users/register.html')