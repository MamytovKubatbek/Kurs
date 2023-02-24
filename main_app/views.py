from django.shortcuts import render, redirect

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
# Create your views here.

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



def index(request):
    box = CategoryBox.objects.all()
    pro=Products.objects.all()
    language = CategoryLanguage.objects.all()

    return render(request, 'index.html',{'pro':pro, 'box': box, 'language': language})



def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context={"form":form}
    return render(request, 'register_form/register.html', context)




def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username Or password is incorrect!! ')
    context={}
    return render(request, 'register_form/login.html', context)



def logautPage(request):
    logout(request)
    return redirect('login')

#===================== Reset Password =====================#

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'register_form/password_reset.html'
    email_template_name = 'register_form/password_reset_email.html'
    # subject_template_name = 'register_form/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')



