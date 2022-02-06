from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    question_one = models.CharField(max_length = 20)
    question_two = models.CharField(max_length = 20)

class RiskAssessmentScore(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    score = models.FloatField()

class Financials(models.Model):
    date =  models.DateTimeField(auto_now = True)
    s_and_p_500 = models.FloatField()
    nasdaq = models.FloatField()
    djia = models.FloatField()


    

