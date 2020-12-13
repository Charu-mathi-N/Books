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
    path(r'main/Pay/', views.Pay, name = 'Pay'),

    path('main/cart_add/<bookID>/', views.cart_add, name='adding'),
    path('Displaycart/cart_remove/<bookID>/', views.cart_remove, name='remove'),
    path('Displaycart/',views.cart_detail, name='cart_detail'),
    path('Displaycart/cart_clear/', views.cart_clear, name='clear'),

    path(r'^$', views.searchposts, name='searchposts'),

    path('api/v1/books/', api_views.BookList.as_view()),
    path('api/v1/books/new', api_views.BookCreate.as_view()),
    path('api/v1/books/<bookId>/', api_views.BookRetrieveUpdateDestroy.as_view()),
    path('premium/', views.premium, name = 'Premium'),
    path('main/Buy_Premium/', views.Buy_Premium, name = 'Buy_Premium'),

]
