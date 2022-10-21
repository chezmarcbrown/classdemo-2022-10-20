from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "users/index.html")
    else:
        return redirect('login')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials. Try again."
            })
    else: 
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", { "message": "Logged out"})
    
from django.db import IntegrityError
from django.contrib.auth.models import User

def register(request):
   if request.method == "POST":
       username = request.POST["username"]
       email = request.POST["email"]

       # Ensure password matches confirmation
       password = request.POST["password"]
       confirmation = request.POST["confirmation"]
       if password != confirmation:
           return render(request, "users/register.html", {
               "message": "Passwords must match."
           })

       # Attempt to create new user
       try:
           user = User.objects.create_user(username, email, password)
           user.save()
       except IntegrityError:
           return render(request, "users/register.html", {
               "message": "Username already taken."
           })
       login(request, user)
       return redirect("index")
   else:
       return render(request, "users/register.html")
       