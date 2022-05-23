from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    question_one = models.CharField(max_length = 20)
    question_two = models.CharField(max_length = 20)

class RiskAssessmentScore(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.SET_NULL)
    score = models.FloatField()
    portfolio_amount = models.FloatField()

class Financials(models.Model):
    date =  models.DateTimeField(auto_now = True)
    s_and_p_500 = models.FloatField()
    nasdaq = models.FloatField()
    djia = models.FloatField()

class StockData(models.Model):
    date =  models.DateTimeField(auto_now = True)
    s_and_p_500 = models.JSONField()
    nasdaq = models.JSONField()
    djia = models.JSONField()

class BenchMarkStockData(models.Model):
    date =  models.DateTimeField(auto_now = True)
    # this actually contains benchmark s_and_p data 
    s_and_p_500_benchmark = models.JSONField()

class MutualFundData(models.Model):
    date =  models.DateTimeField(auto_now = True)
    vanguard = models.JSONField()
    fidelity = models.JSONField()
    schwab = models.JSONField()


class Portfolio(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.SET_NULL)
    # stock_discrete_port is going to be the actual # of shares bought for 
    # each company
    stock_discrete_port = models.JSONField()
    # stock port is the percentage allocated to the individual stock
    stock_port = models.JSONField()
    # mf_discrete_port is going to be the actual # of shares bought for 
    # each mf
    mf_discrete_port = models.JSONField()
    # mf port is the percentage allocated to the individual mf
    mf_port = models.JSONField()
    # crypto_discrete_port is going to be the actual # of shares bought for 
    # each mf
    crypto_discrete_port = models.JSONField(null=True)
    # crypto port is the percentage allocated to the individual mf
    crypto_port = models.JSONField(null=True)

    stock_breakdown = models.FloatField(null=True)
    mf_breakdown = models.FloatField(null=True)
    crypto_breakdown = models.FloatField(null=True)



