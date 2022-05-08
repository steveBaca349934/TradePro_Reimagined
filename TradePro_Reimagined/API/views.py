from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from . import forms, models, utils
from django.db.models import Max
from datetime import datetime
# Create your views here.
from django.views import View
import json

login_form = forms.LoginForm()
account_creation_form = forms.AccountCreationForm()
change_pdub = forms.ChangePDub()
recovery_questions_form = forms.RecoveryQuestions()
recover_account_form = forms.RecoverAccountForm()
rat_form = forms.RiskAssessmentTest()
financial_form = forms.FinacialIndex()
mutual_fund_form = forms.MutualFundProviders()



class BaseView(View):

    # If you want every class based view to have access to some 
    # piece of session data, change it here and then change layout.html
    def __init__(self):

        self.dict = None

    def _setup_view(self,request):
        
        self.dict = {
            "logged_in": request.session.get('logged_in'),
            "user":request.session.get("user")
        }
        
        # need to check most recent date in Financials Model
        # if most recent date is not today, then we need to 
        # update the financials data...
        max_financial_date = models.Financials.objects.aggregate(Max('date'))
        max_date = max_financial_date.get('date__max')
        if (max_date is None) or (max_date.day < datetime.now().day):

            # refresh financials
            financials = utils.scrape_web_data()

            self.dict['finance_data'] = financials

            update_financials = models.Financials.objects.create(s_and_p_500=financials.get('S&P500'),
                                                         nasdaq=financials.get('NASDAQ'), djia = financials.get('DJIA'))

            update_financials.save()

        else:
            
            data = models.Financials.objects.filter(date = max_date)[0]
            financials = {'S&P500': data.s_and_p_500,
                          'NASDAQ': data.nasdaq,
                          'DJIA': data.djia}

            
            self.dict['finance_data'] = financials

            

    def get(self, request):
        self._setup_view(request)
        

        #return render(request, f"home/{html_name}.html",self.dict)

    def post(self, request):
        self._setup_view(request)
        

        #return render(request, f"home/{html_name}.html",self.dict)

class Web3Info(BaseView):

    def get(self, request):
        pass
        
        

    def post(self, request):

        req_res:dict = json.loads(request.body)
        account_num = req_res.get('account_num')

        if len(account_num) == 0:
            return HttpResponse(status=400)

        print(f" \n \n \n the account number is {account_num} \n \n \n ")
        print(f" \n \n \n the type of account number is {type(account_num)} \n \n \n ")



        # this could be incorrect {}
        return HttpResponse(status=200)
        

class RecoverAccount(BaseView):

    def get(self, request):
        super(RecoverAccount, self).get(request)

        # if they're logged in, redirect to profile page
        if not request.user.is_anonymous:

            return HttpResponseRedirect(reverse('profile'))

        self.dict['form'] = recover_account_form
        return render(request, "home/recover_account.html",self.dict)

    def post(self, request):
        super(RecoverAccount, self).post(request)

        #first need to dynamically check and ensure everything was correctly entered
        not_provided = []

        for elem in request.POST:

            if len(request.POST[elem]) == 0:

                not_provided.append(elem.capitalize())

        if len(not_provided) > 0:

            self.dict['form'] = recover_account_form
            self.dict['not_provided'] = not_provided
            return render(request, "home/recover_account.html",self.dict)

        else:
            
            username = request.POST['username']
            question_one = request.POST['question_one']
            question_two = request.POST['question_two']

            # need to get the ID associated with this username
            user_query_res = User.objects.filter(username = username)[0]
            user_id = user_query_res.id
            
            user_email = user_query_res.email
            user_profile_query_res = models.UserProfile.objects.filter(user_id = user_id)[0]

            if (question_one == user_profile_query_res.question_one) and (question_two == user_profile_query_res.question_two):
                self.dict['success'] = True
                self.dict['email'] = user_email
                
                #TODO actually send a recovery email
                return render(request, "home/recover_account.html",self.dict)


        self.dict['form'] = recover_account_form
        return render(request, "home/recover_account.html",self.dict)


        

class Index(BaseView):

    def get(self, request):
        #self._setup_view(request)

        super(Index, self).get(request)

        return render(request, "home/index.html",self.dict)

    def post(self, request):
        pass
    

class Portfolio(BaseView):

    def get(self, request):

        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse('log_in'))

        super(Portfolio, self).get(request)

        query_risk_assessment_score = models.RiskAssessmentScore.objects.filter(user=request.user)

        if len(query_risk_assessment_score) > 0:

            # This is the RAT score
            self.dict['avg_of_scores'] = query_risk_assessment_score[0].score

            # get stock market data and build an optimal portfolio
            # based off of the RAT score
            # s_and_p_tickers = utils.scrape_stock_tickers()
            # data = utils.get_ticker_data(s_and_p_tickers)

            # investment_vehicles_and_alloc:dict = utils.retrieve_optimal_portfolio(data, s_and_p_tickers ,self.dict['avg_of_scores'])

            # for company, allocations in investment_vehicles_and_alloc.items():
            #     investment_vehicles_and_alloc[company] = round(allocations,3)


            # self.dict['investment_vehicles_and_alloc'] = investment_vehicles_and_alloc
            # self.dict['discrete_investment_vehicles_and_alloc'] = utils.retrieve_optimal_portfolio_discrete_allocations(data, s_and_p_tickers, self.dict['avg_of_scores'])
            self.dict['financial_form'] = financial_form
            self.dict['mutual_fund_form'] = mutual_fund_form
         
            return render(request, "home/portfolio.html",self.dict)
            


        else:

            return HttpResponseRedirect(reverse('risk_assessment_test'))

    def post(self, request):
        super(Portfolio, self).post(request)

        query_risk_assessment_model = models.RiskAssessmentScore.objects.filter(user=request.user)

        if len(query_risk_assessment_model) > 0:
            score = query_risk_assessment_model[0].score
            portfolio_amount = query_risk_assessment_model[0].portfolio_amount

            query_stock_data = models.StockData.objects.all()
            query_mutual_fund_data = models.MutualFundData.objects.all()

            print(f"\n the results from querying the stock market data are {query_stock_data} \n ")
            print(f"\n the results from querying the mutual_fund data are {query_mutual_fund_data} \n ")
           

            form = forms.FinacialIndex(request.POST)
            if form.is_valid():
                print(f"\n \n \n the data actually found in the form is {form.cleaned_data.get('Financials')} \n \n \n ")

                res = form.cleaned_data.get('Financials')
                res_dict = {'S&P':False, 'DJIA': False, 'NASDAQ':False}

                for market in res:
                    if market in res_dict:
                        res_dict[market] = True

                print(f"res_dict is {res_dict}")
                
                # get stock market data and build an optimal portfolio
                # based off of the RAT score
                # tickers = utils.scrape_stock_tickers(S_AND_P = res_dict.get('S&P'), NASDAQ = res_dict.get('DJIA'), DJIA = res_dict.get('NASDAQ') )

                # data = utils.get_ticker_data(tickers)

                # investment_vehicles_and_alloc:dict = utils.retrieve_optimal_portfolio(data, tickers ,self.dict['avg_of_scores'])

                # for company, allocations in investment_vehicles_and_alloc.items():
                #     investment_vehicles_and_alloc[company] = round(allocations,3)


                # self.dict['investment_vehicles_and_alloc'] = investment_vehicles_and_alloc
                # self.dict['discrete_investment_vehicles_and_alloc'] = utils.retrieve_optimal_portfolio_discrete_allocations(data, tickers, score, portfolio_amount)


                return render(request, "home/portfolio.html",self.dict)

            else:

                # if the person didn't input the data properly this is an annoynace
                # and we make them do it again lol
                self.dict['financial_form'] = financial_form


                return render(request, "home/portfolio.html",self.dict)


        #TODO: obviously going to need to change this
        return HttpResponseRedirect(reverse('risk_assessment_test'))

class Profile(BaseView):

    def get(self, request):

        super(Profile, self).get(request)

        return render(request, "home/profile.html",self.dict)

    def post(self, request):
        pass


class RAT(BaseView):

    def get(self, request, **kwargs):

        super(RAT, self).get(request)

        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse('log_in'))

        super(RAT, self).get(request)

        reset = kwargs.get('reset')

        if reset == 1:
            models.RiskAssessmentScore.objects.filter(user=request.user).delete()


        query_risk_assessment_score = models.RiskAssessmentScore.objects.filter(user=request.user)

        
        if len(query_risk_assessment_score) > 0:

            self.dict['avg_of_scores'] = query_risk_assessment_score[0].score


            return render(request, "home/rat.html",self.dict)

        else:

            self.dict['rat_form'] = rat_form

            return render(request, "home/rat.html",self.dict)

    
    def post(self, request):
        super(RAT, self).get(request)

        # The last question in the RAT is a question about the total amount of $ the client has to invest
        # We obviously don't want to throw this into the average, because the RAT score is supposed 
        # to be between 1 and 5
        scores = [int(request.POST[question]) for question in request.POST if 'question' in question.lower() and question != 'question_nine']
        avg_of_scores = sum(scores)/len(scores)
        

        self.dict['avg_of_scores'] = avg_of_scores

        rat_score = models.RiskAssessmentScore.objects.create(user=request.user,
                                                         score = avg_of_scores)

        rat_score.save()

        return render(request, "home/rat.html",self.dict)

class ChangePassword(BaseView):
    """
    This is under the requirement that the user
    knows their current password
    """

    def get(self, request):

        if request.user.is_anonymous:

            return HttpResponseRedirect(reverse('log_in'))

        else:

            super(ChangePassword, self).get(request)
            self.dict['new_pw_form'] = change_pdub

            return render(request, "home/change_password.html",self.dict)

    def post(self, request):

        #the user must be logged in before they can use this functionality
        super(ChangePassword, self).post(request)
        self.dict['new_pw_form'] = change_pdub

        old_password = request.POST['old_password']
        new_password = request.POST['new_password']

        # first need to check if the passwords were even submitted
        if len(old_password) == 0:
            self.dict['no_old_password'] = True

            return render(request, "home/change_password.html",self.dict)

        if len(new_password) == 0:

            self.dict['no_new_password'] = True

            return render(request, "home/change_password.html",self.dict)


        # check to see if old password is legit or not
        user = authenticate(request, username=request.session.get("user"), password=old_password)

        if user is None:
            self.dict["wrong_pw"] = True

            return render(request, "home/change_password.html",self.dict)


        else:

            if utils.check_pw_is_robust(new_password):
                #the password is robust enough

                query_res = User.objects.filter(username = request.session.get("user"))[0]

                query_res.password = make_password(new_password)
                query_res.save()

                return HttpResponseRedirect(reverse('index'))

            else:

                self.dict["weak_pw"] = True

                return render(request, "home/change_password.html",self.dict)


class RecoveryQuestions(BaseView):


    def get(self, request):

        # They need to be logged in for this
        if request.user.is_anonymous:

            return HttpResponseRedirect(reverse('log_in'))

        super(RecoveryQuestions,self).get(request)

        self.dict['questions_form'] = recovery_questions_form

        return render(request, "home/recovery_questions.html",self.dict)

    def post(self,request):

        super(RecoveryQuestions,self).post(request)

        question_one = request.POST['question_one']
        question_two = request.POST['question_two']

        #first need to dynamically check and ensure everything was correctly entered
        not_provided = []

        for elem in request.POST:

            if len(request.POST[elem]) == 0:

                not_provided.append(elem.capitalize())

        # in this case, some element was not correctly provided during
        # the users attempt to give recovery questions
        if len(not_provided) > 0:

            self.dict['questions_form'] = recovery_questions_form
            self.dict['not_provided'] = not_provided

            
            return render(request, "home/recovery_questions.html",self.dict)

        else:

            self.dict['success'] = recovery_questions_form

            user_list = models.UserProfile.objects.values_list('user_id', flat = True)

            if request.user.id in user_list:
                # in this case they are already in the UserProfile data base

                # perform update to row of data
                query_res = models.UserProfile.objects.filter(user = request.user)[0]
                query_res.question_one = question_one
                query_res.question_two = question_two

                query_res.save()

            else:


                user_profile = models.UserProfile.objects.create(user=request.user, question_one=question_one,
                                                                                    question_two = question_two)

                user_profile.save()

            return render(request, "home/recovery_questions.html",self.dict)



        return render(request, "home/change_password.html",self.dict)
        


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
    if not request.user.is_anonymous:

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

                # actually logging the user in
                login(request, user)
                
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
    if not request.user.is_anonymous:

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

                    # actually logging the user in
                    login(request, user)
                
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





