from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms, models, utils
# Create your views here.
from django.views import View

login_form = forms.LoginForm()

"""
Global session variables:
    logged_in = boolean value for whether a user is logged in or not
    user = user that is logged in

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

    

    #user.session_set.all().delete()

    # This might not be necessary because Im deleting 
    # the session anyways...
    if 'logged_in' in request.session:

        request.session['logged_in'] = False

    if 'user' in request.session:

        request.session['user'] = None


    # print("the current session user is:")
    # print(request.session.objects.all())
    #request.session.get("user").session_set.all().delete()


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

    else:

        if request.method == 'POST':
            
            email = request.POST['email']
            pw = request.POST['password']

            if len(pw) == 0 and len(email) == 0:

                    return render(request, "home/log_in.html",{
                    "login_form": login_form,
                    "pw_provided": False,
                    "email_provided": False

            })

            
            # First step, ensure that email and 
            # password were both entered        
            elif (len(email) == 0):
                return render(request, "home/log_in.html",{
                "login_form": login_form,
                "email_provided": False

        })

            elif len(pw) == 0:

                return render(request, "home/log_in.html",{
                "login_form": login_form,
                "pw_provided": False

        })

            elif len(pw) >=1 and len(email) >=1:

                all_users = models.User.objects.all()

                emails_to_pws = dict()

                for users in all_users:

                    emails_to_pws[users.email] = users.password

                # actually checking if the email provided 
                # and password are correct            
                if email in emails_to_pws:

                    if emails_to_pws[email] == pw:

                        request.session['user'] = email
                        request.session['logged_in'] = True

                    
                        return render(request, "home/log_in.html",{

                                "login_form": login_form,
                                "logged_in_bool": True,
                                "user": email

                                })

                    else:

                        return render(request, "home/log_in.html",{

                        "login_form": login_form,
                        "incorrect_pw": True
                        })

                else:

                    return render(request, "home/log_in.html",{

                        "login_form": login_form,
                        "email_not_found": True,
                        "user": email
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
        pw = request.POST['password']
        email = request.POST['email']

        if len(pw) == 0 and len(email) == 0:

                return render(request, "home/open_an_account.html",{
                "newacc_form": login_form,
                "pw_provided": False,
                "email_provided": False

        })

        
        # First step, ensure that email and 
        # password were both entered        
        elif (len(email) == 0):
            return render(request, "home/open_an_account.html",{
            "newacc_form": login_form,
            "email_provided": False

    })

        elif len(pw) == 0:

            return render(request, "home/open_an_account.html",{
            "newacc_form": login_form,
            "pw_provided": False

    })

        elif len(pw) >=1 and len(email) >=1:
            #need to check if this user's email is already in the database

            all_users = models.User.objects.all()

            cur_emails = set()

            for users in all_users:
                cur_emails.add(users.email)

            if email in cur_emails:

                return render(request, "home/open_an_account.html",{
                "newacc_form": login_form,
                "email_taken": True

                })

            else:

                new_user = models.User(email = email, password = pw)
                new_user.save()


            
            
            

        return render(request, "home/open_an_account.html",{
        "newacc_form": login_form



    })

def profile(request):

    return render(request, "home/profile.html")

def risk_assessment_test(request):

    return render(request, "home/rat.html")