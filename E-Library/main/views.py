from .models import Books
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import views as auth_views
from . import views
from django.db import models
from django.db.models import Model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CartAddBookForm
from .cart import Cart

from django.db.models import Q

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

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(Title__icontains=query) | Q(Authors__icontains=query)

            results= Books.objects.filter(lookups).distinct()
            messages.success(request, "Found books")

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'main/header.html', context)

        else:
            return render(request, 'main/header.html')

    else:
        return render(request, 'main/home.html')

def Pay(request):
    return render(request, 'main/Pay.html')

@login_required
@require_POST
def cart_add(request, bookID):
    cart = Cart(request)
    book = get_object_or_404(Books, id=bookID)
    form = CartAddBookForm(request.POST)
    messages.success(request, "Successfully Added to Cart")
    cart.add(book=book,
            quantity = 1)
    return redirect('main:cart_detail')

def cart_remove(request, bookID):
    cart = Cart(request)
    book = get_object_or_404(Books, id=bookID)
    cart.remove(book)
    messages.info(request, "Removed Item Successfully")
    return redirect('main:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/Displaycart.html', {'cart': cart})

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.info(request, "Cart Cleared Successfully")
    return redirect("main:cart_detail")


@login_required
def premium(request):
    return render(request, 'main/premium.html')

@login_required
def Buy_Premium(request):
    return render(request, 'main/Buy_Premium.html')

# def checkout(request, bookID):
#     books = Books.objects.get(id = bookID)
#     return render(request, 'main/Buy_Premium.html', {'books': books,})


