from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import smtplib

app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path(r'main/Buy/<bookID>/', views.Buy, name = 'buy'),
    path('admin/', admin.site.urls),
    #path("", views.homepage, name = "Homepage"),
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
    path(r'main/Pay/<bookID>/', views.Pay, name = 'Pay')
    path(r'main/Cart/<bookID>/', views.Cart, name = 'Cart')
]
