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

class PortfolioHistoricalReturns(Portfolio):

    def get(self, request):

        super(Portfolio, self).get(request)
        super(Portfolio, self).post(request)


        query_benchmark_data = models.BenchMarkStockData.objects.all()

        s_and_p_benchmark_df = utils.retrieve_and_clean_benchmark_data(query_benchmark_data)

        s_and_p_benchmark_with_returns_df = utils.calculate_percentage_returns_for_benchmark(s_and_p_benchmark_df)


        return render(request, "home/portfolio_historical_returns.html",self.dict)

    def post(self, request):

        super(Portfolio, self).post(request)

        return render(request, "home/portfolio_historical_returns.html",self.dict)


