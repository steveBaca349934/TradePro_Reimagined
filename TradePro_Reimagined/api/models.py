from django.db import models

# Create your models here.
from django.db import models

class RecoveryQuestions(models.Model):
    question_one = models.CharField(max_length = 20)
    question_two = models.CharField(max_length = 20)


    

