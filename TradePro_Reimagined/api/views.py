from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms
# Create your views here.


# Create your views here.
def index(request):

    return render(request, "home/index.html")

def customer_service(request):

    return render(request, "home/customer_service.html")

def log_in(request):

    email_form = forms.EmailForm()
    pw_form = forms.PasswordForm()

    return render(request, "home/log_in.html",{
        "email_form": email_form,
        "pw_form": pw_form


    })

def add_email(request):

    pass

def add_pw(request):

    pass

def open_an_account(request):

    return render(request, "home/open_an_account.html")

def profile(request):

    return render(request, "home/profile.html")

def risk_assessment_test(request):

    return render(request, "home/rat.html")