from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms, models
# Create your views here.

login_form = forms.LoginForm()

# Create your views here.
def index(request):

    return render(request, "home/index.html")

def customer_service(request):

    return render(request, "home/customer_service.html")

def log_in(request):


    return render(request, "home/log_in.html",{
        "login_form": login_form,
        "logged_in_bool": False,
        "user": " "

    })

def add_email_and_pw(request):

    if request.method == 'POST':

        email = request.POST['email']
        
        return render(request, "home/log_in.html",{

        "login_form": login_form,
        "logged_in_bool": True,
        "user": email
        })


def open_an_account(request):

    return render(request, "home/open_an_account.html")

def profile(request):

    return render(request, "home/profile.html")

def risk_assessment_test(request):

    return render(request, "home/rat.html")