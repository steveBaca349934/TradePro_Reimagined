from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms, models, utils
# Create your views here.
from django.views import View

login_form = forms.LoginForm()
account_creation_form = forms.AccountCreationForm()

"""
Global session variables:
    logged_in = boolean value for whether a user is logged in or not
    user = username that is logged in
    email = email that is logged in

"""

# Create your views here.
def index(request):


    return render(request, "home/index.html",{
            "logged_in": request.session.get('logged_in'),
            "user":request.session.get("user")
    })
    
    
def customer_service(request):

    return render(request, "home/customer_service.html",{
        "logged_in": request.session.get('logged_in'),
        "user":request.session.get("user")
    })

def log_out(request):
    """
    Sets the session variables for logged in to false
    and user to None

    Note * They are still technically in the same session

    redirects to the home page
    """

    if 'logged_in' in request.session:

        request.session['logged_in'] = False

    if 'user' in request.session:

        request.session['user'] = None


    # return to the homepage
    return index(request)


def log_in(request):
    """
    provides functionality to allow a user to login

    returns the login page with either success or failure message
    """

    # First check to see if a user is logged in 
    if request.session.get('logged_in'):

        return render(request, "home/log_in.html",{

        # "login_form": login_form,
        "logged_in": request.session.get('logged_in'),
        "user":request.session.get("user")
        })

    # if the user isn't logged in, need to help them 
    # login
    elif request.method == 'POST':

        username = request.POST['username']
        pw = request.POST['password']

        #first need to dynamically check and ensure everything was correctly entered
        not_provided = []

        for elem in request.POST:

            if len(request.POST[elem]) == 0:

                not_provided.append(elem.capitalize())

        # in this case, some element was not correctly provided during
        # the users attempt to login
        if len(not_provided) > 0:
            
            return render(request, "home/log_in.html",{
                    "login_form": login_form,
                    "not_provided": not_provided

            })

        # the user entered both a password and username
        else:

            user = authenticate(request, username=username, password=pw)

            if user is not None:
                
                request.session['user'] = username
                request.session['logged_in'] = True

                return render(request, "home/log_in.html",{

                        "login_form": login_form,
                        "logged_in": request.session.get('logged_in'),
                        "user":request.session.get("user")
                        })

            # the authentication failed
            else:

                return render(request, "home/log_in.html",{

                "login_form": login_form,
                "incorrect_pw": True
                })

        
    return render(request, "home/log_in.html",{

         "login_form": login_form,
        "logged_in": request.session.get('logged_in'),
        "user":request.session.get("user")
        })




def open_an_account(request):
    """
    Basic rendering of open_an_account page

    returns render
    """

    #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    # username
    # password
    # email
    # first_name
    # last_name

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        pw = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        
        not_provided = []

        for elem in request.POST:

            if len(request.POST[elem]) == 0:

                not_provided.append(elem)

        # in this case, some element was not correctly provideds
        if len(not_provided) > 0:

            return render(request, "home/open_an_account.html",{
                "newacc_form": account_creation_form,
                "not_provided": not_provided

        })


    #     elif len(pw) >=1 and len(email) >=1:
    #         #need to check if this user's email is already in the database

    #         all_users = models.User.objects.all()

    #         cur_emails = set()

    #         for users in all_users:
    #             cur_emails.add(users.email)

    #         if email in cur_emails:

    #             return render(request, "home/open_an_account.html",{
    #             "newacc_form": login_form,
    #             "email_taken": True

    #             })

    #         else:

    #             new_user = models.User(email = email, password = pw)
    #             new_user.save()



    return render(request, "home/open_an_account.html",{
        "newacc_form": account_creation_form

    })


def profile(request):

    return render(request, "home/profile.html")

def risk_assessment_test(request):

    return render(request, "home/rat.html")