from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
#from .forms import *
# Create your views here.


# Create your views here.
def index(request):

    return render(request, "home/index.html")

def customer_service(request):

    return render(request, "home/customer_service.html")

def log_in(request):

    return render(request, "home/log_in.html")

def open_an_account(request):

    return render(request, "home/open_an_account.html")

def profile(request):

    return render(request, "home/profile.html")