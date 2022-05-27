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
import pandas as pd

from API.views import Portfolio

class PortfolioHistoricalReturns(Portfolio):

    def get(self, request):

        super(Portfolio, self).get(request)
        
        query_benchmark_data = models.BenchMarkStockData.objects.all()

        s_and_p_benchmark_df = utils.retrieve_and_clean_benchmark_data(query_benchmark_data)

        s_and_p_benchmark_with_returns_df = utils.calculate_percentage_returns_for_benchmark(s_and_p_benchmark_df)

        # Now need to query users portfolio allocations so I can compare them to the benchmark
        query_portfolio = models.Portfolio.objects.filter(user = request.user)
        if len(query_portfolio) > 0:

            stock_port = query_portfolio[0].stock_port
            mf_port = query_portfolio[0].mf_port

            stock_port_dict = json.loads(stock_port)
            mf_port_dict = json.loads(mf_port)

            query_stock_data = models.StockData.objects.all()
            query_mf_data = models.MutualFundData.objects.all()

            stock_df = utils.extract_historical_data_for_specific_stock_tickers(stock_port_dict
                                                                               ,query_stock_data)
            stock_df.fillna(0.0, inplace=True)

            mf_df = utils.extract_historical_data_for_specific_mf_tickers(mf_port_dict
                                                                      ,query_mf_data)
            

            stock_w_percentage_returns_df = utils.calculate_percentage_returns_for_df(stock_df)

            mf_w_percentage_returns_df = utils.calculate_percentage_returns_for_df(mf_df)

            stock_breakdown = query_portfolio[0].stock_breakdown
            mf_breakdown = query_portfolio[0].mf_breakdown
            crypto_breakdown = query_portfolio[0].crypto_breakdown

            print(f"\n stock_breakdown is {stock_breakdown} \n")
            print(f"\n mf_breakdown is {mf_breakdown} \n")
            print(f"\n crypto_breakdown is {crypto_breakdown} \n")

            # the formula to correctly calculate the returns for the portfolio
            # is the sum of the weighted returns for each asset
            # including the stock/mf/crypto breakdown

            stock_weighted_percentage_returns_df = utils.calculate_weighted_percentage_returns(stock_port_dict
                                                                                      ,stock_w_percentage_returns_df
                                                                                      ,stock_breakdown)

            mf_weighted_percentage_returns_df = utils.calculate_weighted_percentage_returns(mf_port_dict
                                                                                           ,mf_w_percentage_returns_df
                                                                                           ,mf_breakdown)

            
            # Massive TODO: Need to integrate Crypto into the portfolio
            final_df = pd.DataFrame()
            final_df['Date'] = mf_weighted_percentage_returns_df['Date']
            final_df['Portfolio_Returns'] = mf_weighted_percentage_returns_df['Sum_Weighted_Returns'] \
                                            + stock_weighted_percentage_returns_df['Sum_Weighted_Returns']
                                            # eventually add crypto as well
            
            final_df['BenchMark_Returns'] = s_and_p_benchmark_with_returns_df['s_and_p_benchmark']

            
            query_risk_assessment_model = models.RiskAssessmentScore.objects.filter(user=request.user)
            portfolio_amount = query_risk_assessment_model[0].portfolio_amount

            final_df = utils.calculate_dollar_returns(portfolio_amount, final_df)

            self.dict['Portfolio_Returns'] = json.dumps(utils.prepare_for_jsonify_portfolio_data(final_df[['Date','Portfolio_Returns']]
                                                                                                ,'Portfolio_Returns'))
            self.dict['BenchMark_Returns'] = json.dumps(utils.prepare_for_jsonify_portfolio_data(final_df[['Date','BenchMark_Returns']]
                                                                                                ,'BenchMark_Returns'))

            


        return render(request, "home/portfolio_historical_returns.html",self.dict)

    def post(self, request):

        super(Portfolio, self).post(request)



        return render(request, "home/portfolio_historical_returns.html",self.dict)



class PortfolioHistoricalDollarReturns(Portfolio):

    def get(self, request):

        super(Portfolio, self).get(request)
        
        query_benchmark_data = models.BenchMarkStockData.objects.all()

        s_and_p_benchmark_df = utils.retrieve_and_clean_benchmark_data(query_benchmark_data)

        s_and_p_benchmark_with_returns_df = utils.calculate_percentage_returns_for_benchmark(s_and_p_benchmark_df)

        # Now need to query users portfolio allocations so I can compare them to the benchmark
        query_portfolio = models.Portfolio.objects.filter(user = request.user)
        if len(query_portfolio) > 0:

            stock_port = query_portfolio[0].stock_port
            mf_port = query_portfolio[0].mf_port

            stock_port_dict = json.loads(stock_port)
            mf_port_dict = json.loads(mf_port)

            query_stock_data = models.StockData.objects.all()
            query_mf_data = models.MutualFundData.objects.all()

            stock_df = utils.extract_historical_data_for_specific_stock_tickers(stock_port_dict
                                                                               ,query_stock_data)
            stock_df.fillna(0.0, inplace=True)

            mf_df = utils.extract_historical_data_for_specific_mf_tickers(mf_port_dict
                                                                      ,query_mf_data)
            

            stock_w_percentage_returns_df = utils.calculate_percentage_returns_for_df(stock_df)

            mf_w_percentage_returns_df = utils.calculate_percentage_returns_for_df(mf_df)

            stock_breakdown = query_portfolio[0].stock_breakdown
            mf_breakdown = query_portfolio[0].mf_breakdown
            crypto_breakdown = query_portfolio[0].crypto_breakdown

            print(f"\n stock_breakdown is {stock_breakdown} \n")
            print(f"\n mf_breakdown is {mf_breakdown} \n")
            print(f"\n crypto_breakdown is {crypto_breakdown} \n")

            # the formula to correctly calculate the returns for the portfolio
            # is the sum of the weighted returns for each asset
            # including the stock/mf/crypto breakdown

            stock_weighted_percentage_returns_df = utils.calculate_weighted_percentage_returns(stock_port_dict
                                                                                      ,stock_w_percentage_returns_df
                                                                                      ,stock_breakdown)

            mf_weighted_percentage_returns_df = utils.calculate_weighted_percentage_returns(mf_port_dict
                                                                                           ,mf_w_percentage_returns_df
                                                                                           ,mf_breakdown)

            
            # Massive TODO: Need to integrate Crypto into the portfolio
            final_df = pd.DataFrame()
            final_df['Date'] = mf_weighted_percentage_returns_df['Date']
            final_df['Portfolio_Returns'] = mf_weighted_percentage_returns_df['Sum_Weighted_Returns'] \
                                            + stock_weighted_percentage_returns_df['Sum_Weighted_Returns']
                                            # eventually add crypto as well
            
            final_df['BenchMark_Returns'] = s_and_p_benchmark_with_returns_df['s_and_p_benchmark']

            
            query_risk_assessment_model = models.RiskAssessmentScore.objects.filter(user=request.user)
            portfolio_amount = query_risk_assessment_model[0].portfolio_amount

            final_df = utils.calculate_dollar_returns(portfolio_amount, final_df)

            self.dict['Dollar_Portfolio_Returns'] = json.dumps(utils.prepare_for_jsonify_portfolio_data(final_df[['Date','Dollar_Portfolio_Returns']]
                                                                                                ,'Dollar_Portfolio_Returns'))
            self.dict['Dollar_BenchMark_Returns'] = json.dumps(utils.prepare_for_jsonify_portfolio_data(final_df[['Date','Dollar_Benchmark_Returns']]
                                                                                                ,'Dollar_Benchmark_Returns'))




        return render(request, "home/portfolio_historical_dollar_returns.html",self.dict)

    def post(self, request):

        super(Portfolio, self).post(request)



        return render(request, "home/portfolio_historical_dollar_returns.html",self.dict)





