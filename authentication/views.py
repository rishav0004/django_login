from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,'authentication/index.html')


def signin(request):

    if request.method =="POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        user = authenticate(username = username, password = password1)

        if user is not None:
            login(request,user)
            fname = User.first_name
            return render(request,'authentication/index.html',{'fname':fname})
        
        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')

    return render(request,'authentication/signin.html')


def signup(request):
    if request.method =="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'You are successfully signed up')

        return redirect('signin')


    return render(request,'authentication/signup.html')


def signout(request):
    logout(request)
    messages.success(request,"You're successfully logged out" )
    return redirect('home')


def sending_mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name,subject,email,message)

        send_mail(
            subject,
            message,
            'rishabh55.mahajan@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request,'Mail sent , Thank you for choosing us!')
        return redirect('home')
    
    else:
        return render(request,'authentication/sendmail.html')


