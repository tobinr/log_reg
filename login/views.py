from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'index.html')

def success_page(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, 'success.html')

def register_user(request):
    # print(request.POST)
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else: 
            pw_hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first_name = request.POST['fname'],
                last_name = request.POST['lname'],
                email = request.POST['email'],
                password = pw_hash
            )
            request.session['user'] = request.POST['fname']
            request.session['status'] = "registered"
            print(new_user, "is a new user")
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
                request.session['user'] = logged_user.first_name
                request.session['status'] = "logged in"
                print(logged_user, "was successfully logged in")
                return redirect('/success')
        return redirect('/')
    return redirect('/')


def logout(request):
    print(request.session['user'], "has been successfully logged out")
    request.session.flush()
    print("Session has been flushed")
    return redirect('/')