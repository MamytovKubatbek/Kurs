"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from main.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from main_app.views import ResetPasswordView
from django.contrib.auth import views as auth_views

from main_app.views import * 

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),

    path('login/', loginPage, name='login'),
    path('register/', register, name='register'), 
    path('logautPage/', logautPage, name='logautPage'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='register_form/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='register_form/password_reset_complete.html'),
         name='password_reset_complete'),
]
urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)