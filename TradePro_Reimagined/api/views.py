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

def add_email_and_pw_login(request):
    """
    provides functionality to allow a user to login

    returns the login page with either success or failure message
    """
    # TODO: Actually take email and password and check vs models.py that this is an actual user
    # Also need to percolate and persist across this users entire session

    if request.method == 'POST':

        email = request.POST['email']
        
        return render(request, "home/log_in.html",{

        "login_form": login_form,
        "logged_in_bool": True,
        "user": email
        })


def open_an_account(request):
    """
    Basic rendering of open_an_account page

    returns render
    """


    return render(request, "home/open_an_account.html",{
        "newacc_form": login_form



    })

def add_email_and_pw_newacc(request):
    """
    Provides functionality that allows a user
    to actually create an account... adds email and pw
    to database

    returns render
    """

    if request.method == 'POST':

        print(request.POST)

        if len(request.POST['password']) == 0 and len(request.POST['email']) == 0:

                return render(request, "home/open_an_account.html",{
                "newacc_form": login_form,
                "pw_provided": False,
                "email_provided": False

        })

        
        # First step, ensure that email and 
        # password were both entered        
        if (len(request.POST['email']) == 0):
            return render(request, "home/open_an_account.html",{
            "newacc_form": login_form,
            "email_provided": False

    })

        if len(request.POST['password']) == 0:

            return render(request, "home/open_an_account.html",{
            "newacc_form": login_form,
            "pw_provided": False

    })

        
            

        return render(request, "home/open_an_account.html",{
        "newacc_form": login_form



    })

def profile(request):

    return render(request, "home/profile.html")

def risk_assessment_test(request):

    return render(request, "home/rat.html")