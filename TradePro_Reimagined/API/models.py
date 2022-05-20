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



