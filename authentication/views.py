from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "authentication/index.html")


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['passw']
        fname = request.POST['fname']

# FLAW 2:
#        validate_password(password)

        myuser = User.objects.create_user(username=username, password=password)

        myuser.first_name = fname
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        
        return redirect('signin')
    else:
        return render(request, "authentication/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        passw = request.POST['passw']
        
        user = authenticate(username=username, password=passw)

        if user is not None:
# FLAW 5:
#            logger.info(f"Succesful login for user {username}")
            login(request, user)
            return redirect('home')
        else:
# FLAW 5:
#            logger.warning(f"Failed login attempt for user {username}")
            messages.error(request, "Bad credentials!")
            return redirect('home')
    else:
        return render(request, "authentication/signin.html")


def signout(request):
# FLAW 5:
#    logger.info(f"Succesful logout for user {request.user.username}")
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
