from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import smtplib
from . import api_views

app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path(r'main/Buy/<bookID>/', views.Buy, name = 'buy'),
    path('admin/', admin.site.urls),
    path("login/", views.login_request, name = "Login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(template_name = 'main/Reset.html'),
        name='admin_password_reset',
    ),
    path(
        'admin/password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name = 'main/password_sent.html'),
        name='admin_password_sent',
    ),
    path(
        'password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name = 'main/password_complete.html'),
        name='password_complete',
    ),
    path(r'main/Pay/<bookID>/', views.Pay, name = 'Pay'),
    #path('Displaycart/', views.Display_Cart, name = 'Display_Cart'),


    path('main/cart_add/<bookID>/', views.cart_add, name='adding'),
    path('Displaycart/cart_remove/<bookID>/', views.cart_remove, name='remove'),
    path('Displaycart/',views.cart_detail, name='cart_detail'),
    path('Displaycart/cart_clear/', views.cart_clear, name='clear'),

    # path('cart/item_clear/<int:bookID>/', views.item_clear, name='item_clear'),
    # path('cart/item_increment/<int:bookID>/',
    #      views.item_increment, name='item_increment'),
    # path('cart_clear/', views.cart_clear, name='cart_clear'),


    path('api/v1/books/', api_views.BookList.as_view()),
    path('api/v1/books/new', api_views.BookCreate.as_view()),
    path('api/v1/books/<bookId>/', api_views.BookRetrieveUpdateDestroy.as_view()),
    path('premium/', views.premium, name = 'Premium'),
    path('Buy_Premium/', views.Buy_Premium, name = 'Buy_Premium'),

]
