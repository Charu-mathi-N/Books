from .models import Books
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import views as auth_views
from . import views
from django.db import models
from django.db.models import Model


# Create your views here.
def home(request):
    books = Books.objects.all()
    return render(request, 'main/home.html', {'books': books,})

def Buy(request, bookID):
    books = Books.objects.get(id = bookID)
    return render(request, 'main/buy.html', {'books': books,})

def register(request):

    if request.method == "POST":
        Form = NewUserForm(request.POST)
        if Form.is_valid():
            user = Form.save()
            username = Form.cleaned_data.get('username')
            print("Successfully Registered")
            messages.success(request, f"Successfully Registered: {username}")
            login(request, user)
            return redirect("main:home")
        else:
            for msg in Form.error_messages:
                messages.error(request, f"{msg}: {Form.error_messages[msg]}")
                return render(request = request,
                        template_name = "main/register.html",
                        context = {"form" : Form})

    Form = NewUserForm
    return render(request = request,
                    template_name = "main/register.html",
                    context = {"form" : Form})


def login_request(request):
    if request.method == "POST":
        Form = AuthenticationForm(request, data = request.POST)
        if Form.is_valid():
            username = Form.cleaned_data.get('username')
            password = Form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                messages.success(request, f"Successfully Loggin: {username}")
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
                messages.error(request, "Invalid username or password")
    Form = AuthenticationForm()
    return render(request, "main/login.html", {"form": Form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Successfully")
    print("Logged out Successfully")
    return redirect("main:home")

def Reset(request):

    if request.method == 'POST':
        Form = models.EmailField(request, data = request.POST)
        if Form.is_valid():
            email = Form.cleaned_data.get('email')
            if email is not None:
                messages.success(request, f"Sending reset link to: {email}")
                return render(request, "main/Reset.html", {'form': Form})
            else:
                messages.error(request, "Invalid email_id")
        else:
            messages.error(request, "Invalid email_id")
    return render(request, 'main/Reset.html')

def Pay(request, bookID):
    books = Books.objects.get(id = bookID)
    return render(request, 'main/Pay.html', {'books': books,})

def Cart(request, bookID):
    books = Books.objects.get(id = bookID)
    return render(request, 'main/Cart.html', {'books': books,})
