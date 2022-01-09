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

class BaseView(View):

    # If you want every class based view to have access to some 
    # piece of session data, change it here and then change layout.html

    def _setup_view(self,request):

        self.dict = {
            "logged_in": request.session.get('logged_in'),
            "user":request.session.get("user")
        }

    
    def get(self, request):
        self._setup_view(request)
        

        #return render(request, f"home/{html_name}.html",self.dict)

    def post(self, request):
        self._setup_view(request)
        

        #return render(request, f"home/{html_name}.html",self.dict)

class Index(BaseView):

    def get(self, request):
        self._setup_view(request)

        return render(request, "home/index.html",self.dict)

    def post(self, request):
        pass
    

class CustomerService(BaseView):

    def get(self, request):
        self._setup_view(request)

        return render(request, "home/customer_service.html",self.dict)

    def post(self, request):
        pass

class Profile(BaseView):

    def get(self, request):

        self._setup_view(request)

        return render(request, "home/profile.html",self.dict)

    def post(self, request):
        pass

class RAT(BaseView):

    def get(self, request):

        self._setup_view(request)

        return render(request, "home/rat.html",self.dict)

    def post(self, request):
        pass

def log_out(request):
    """
    Sets the session variables for logged in to false
    and user to None

    Note * They are still technically in the same session

    redirects to the home page
    """
    # built in django command to clear session
    logout(request)


    # redirect to the home page
    return HttpResponseRedirect(reverse('index'))


def log_in(request):
    """
    provides functionality to allow a user to login

    returns the login page with either success or failure message
    """

    # First check to see if a user is logged in 
    if request.session.get('logged_in'):

        return HttpResponseRedirect(reverse('index'))

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

                #redirect to home page
                return HttpResponseRedirect(reverse('index'))

            # authentication failed logic
            else:

                username_list = User.objects.values_list('username', flat = True)
                
                # the username was not valid
                if username not in username_list:

                    return render(request, "home/log_in.html",{

                    "login_form": login_form,
                    "incorrect_user": True,
                    "attempted_user": username
                    })

                # the password was not valid
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
    Rendering of open_an_account page. Also
    handles logic for creating a user. Enforces
    that there must be unique username and email

    returns render
    """

    # if the user is already logged in, just redirect to home page
    if request.session.get('logged_in') == True:

        return HttpResponseRedirect(reverse('index'))



    elif request.method == 'POST':

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
                "not_provided": not_provided,
                "successful_creation": False

        })


        else:

            #need to check if this user's email is already in the database
            cur_emails = User.objects.values_list('email', flat = True)
            cur_usernames = User.objects.values_list('username', flat = True)

            # in this case the email and username are both taken                      
            if (email in cur_emails) and (username in cur_usernames):

                return render(request, "home/open_an_account.html",{
                "newacc_form": account_creation_form,
                "email_taken": True,
                "email":email,
                "username_taken": True,
                "username":username,
                "successful_creation": False


                })

            # in this case the username is taken
            elif username in cur_usernames:

                return render(request, "home/open_an_account.html",{
                "newacc_form": account_creation_form,
                "email_taken": False,
                "email":email,
                "username_taken": True,
                "username":username,
                "successful_creation": False


                })

            # in this case the email is taken
            elif email in cur_emails:

                return render(request, "home/open_an_account.html",{
                "newacc_form": account_creation_form,
                "email_taken": True,
                "email":email,
                "username_taken": False,
                "username":username,
                "successful_creation": False

                })    

            elif utils.check_pw_is_robust(pw) == False:

                #return prescription for more advanced PW

                return render(request, "home/open_an_account.html",{
                "newacc_form": account_creation_form,
                "email_taken": False,
                "email" :email,
                "username_taken": False,
                "username":username,
                "incorrect_pw_format" :True,
                "successful_creation": False

                }) 
                


            else:
                
                #else we can actually create a new user
                new_user = User.objects.create_user(username, email = email, password = pw)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()

                # log user in
                user = authenticate(request, username=username, password=pw)

                if user is not None:
                
                    request.session['user'] = username
                    request.session['logged_in'] = True

                    # redirect to the home page
                    return HttpResponseRedirect(reverse('index'))

                # the authentication failed
                else:

                    return render(request, "home/log_in.html",{

                    "login_form": login_form,
                    "incorrect_pw": True
                    })



    return render(request, "home/open_an_account.html",{
        "newacc_form": account_creation_form

    })


