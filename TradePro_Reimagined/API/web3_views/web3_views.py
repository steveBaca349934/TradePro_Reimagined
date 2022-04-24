from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from API. import forms, models, utils
from django.db.models import Max
from datetime import datetime
# Create your views here.
from django.views import View
import json




class Web3_Home(View):

    def get(self, request):
        # super(Web3_Home,self).get(request)

        print(f"\n \n \n the session user is : {request.session.get('user')} \n \n ")
        self.dict = {"user":request.session.get("user"),
                     "logged_in": request.session.get('logged_in')}

        return render(request, "home/web3_home.html",self.dict)

        

        

    def post(self, request):

        pass

class Web3_Social(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

class Web3_Portfolio(View):

    def get(self, request):
        pass

    def post(self, request):
        pass