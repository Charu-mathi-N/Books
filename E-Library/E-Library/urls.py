"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views as auth_views
#import smtplib

app_name = 'main'

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path("", views.homepage, name = "Homepage"),
    # path("login/", views.login_request, name = "Login"),
    # path("register/", views.register, name="register"),
    # path("logout/", views.logout_request, name= "Logout"),
    # path(
    #     'admin/password_reset/',
    #     auth_views.PasswordResetView.as_view(template_name = 'main/Reset.html'),
    #     name='admin_password_reset',
    # ),
    # path(
    #     'admin/password_sent/',
    #     auth_views.PasswordResetDoneView.as_view(template_name = 'main/password_sent.html'),
    #     name='admin_password_sent',
    # ),
    # path(
    #     'password_reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_confirm',
    # ),
    # path(
    #     'reset/done/',
    #     auth_views.PasswordResetCompleteView.as_view(template_name = 'main/password_complete.html'),
    #     name='password_complete',
    # ),
]



# from django.urls import path, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]