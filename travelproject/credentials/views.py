from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        user=request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=user,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid user name")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('/')

    return render(request, 'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')