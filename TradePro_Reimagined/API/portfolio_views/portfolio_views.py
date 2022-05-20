from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from API import forms, models, utils
from django.db.models import Max
from datetime import datetime
# Create your views here.
from django.views import View
import json

from API.views import Portfolio

login_form = forms.LoginForm()
account_creation_form = forms.AccountCreationForm()
change_pdub = forms.ChangePDub()
recovery_questions_form = forms.RecoveryQuestions()
recover_account_form = forms.RecoverAccountForm()
rat_form = forms.RiskAssessmentTest()
financial_form = forms.FinacialIndex()
mutual_fund_form = forms.MutualFundProviders()


class PortfolioHistoricalReturns(Portfolio):

    def get(self, request):

        super(Portfolio, self).get(request)

        return render(request, "home/portfolio_historical_returns.html",self.dict)

    def post(self, request):

        super(Portfolio, self).post(request)

        return render(request, "home/portfolio_historical_returns.html",self.dict)


