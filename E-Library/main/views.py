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
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CartAddBookForm
from .cart import Cart

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

@login_required
@require_POST
def cart_add(request, bookID):
    cart = Cart(request)
    book = get_object_or_404(Books, id=bookID)
    form = CartAddBookForm(request.POST)
    cart.add(book=book,
            quantity = 1)
    return redirect('main:cart_detail')

def cart_remove(request, bookID):
    cart = Cart(request)
    book = get_object_or_404(Books, id=bookID)
    cart.remove(book)
    return redirect('main:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddBookForm(
    #                       initial={'quantity': item['quantity'],
    #                       'update': True})

    return render(request, 'main/Displaycart.html', {'cart': cart})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("main:cart_detail")


# def product_detail(request, id, slug):
#     book = get_object_or_404(Book, id=id,
#                                          slug=slug,
#                                          available=True)

#     cart_product_form = CartAddBookForm()

#     return render(request,
#                   'shop/product/detail.html',
#                   {'book': book,

# 'cart_product_form': cart_product_form



# })

# def cart_add(request, bookID):
#     cart = Cart(request)
#     product = Books.objects.get(id = bookID)
#     cart.add(product)
#     return redirect("main:home")

# @login_required
# def cart_add(request, bookID):
#     cart = Cart(request)
#     product = get_object_or_404(Books, id=bookID)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')


# @login_required
# def remove(request, id):
#     cart = Cart(request)
#     books = Books.objects.get(id = bookID)
#     cart.remove(bookID)
#     return redirect("main:home")


# @login_required
# def item_increment(request, id):
#     cart = Cart(request)
#     books = Books.objects.get(id = bookID)
#     cart.add(bookID)
#     return redirect("main:home")


# @login_required
# def item_decrement(request, id):
#     cart = Cart(request)
#     books = Books.objects.get(id = bookID)
#     cart.decrement(bookID)
#     return redirect("main:home")


# @login_required
# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("main:home")

# @login_required
# def cart_detail(request):
#     return redirect("main:home")

# def cart_add(request, bookID):
#     book_id = int(bookID)
#     book = get_object_or_404(Books, pk=bookID)
#     cart,created = Cart.objects.get_or_create(user=request.user)
#     cart.add(bookID)
#     return redirect('home')

# @login_required
# def cart_add(request, bookID):
#     book = get_object_or_404(Books, pk=bookID)
#     cart,created = Cart.objects.get_or_create(user=request.user, active=True)
#     #order,created = BookOrder.objects.get_or_create(book=book,cart=cart)
#     #order.quantity += 1
#     #order.save()
#     messages.success(request, "Cart updated!")
#     return redirect('main:home')

# def cart_add(request, bookID):
#     cart = Cart(request)
#     books = Books.objects.get(id=bookID)
#     cart.add()
#     cart.add_to_cart(bookID)
#     return redirect("home")


# @login_required
# def item_clear(request, bookID):
#     cart = Cart(request)
#     books = Books.objects.get(id=bookID)
#     cart.remove(books)
#     return redirect("cart_detail")


# @login_required
# def item_increment(request, bookID):
#     cart = Cart(request)
#     books = Books.objects.get(id=bookID)
#     cart.add(books=books)
#     return redirect("main:home")


# @login_required
# def item_decrement(request, bookID):
#     cart = Cart(request)
#     books = Books.objects.get(id=bookID)
#     cart.decrement(books=books)
#     return redirect("cart_detail")


# @login_required
# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("cart_detail")


# @login_required
# def cart_detail(request):
#     return render(request, 'cart/cart_detail.html')

def premium(request):
    return render(request, 'main/premium.html')

def Buy_Premium(request):
    return render(request, 'main/Buy_Premium.html')

