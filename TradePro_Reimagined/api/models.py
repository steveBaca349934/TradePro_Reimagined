from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    email = models.CharField(max_length = 18)
    password = models.CharField(max_length = 18)
    #age = models.IntegerField()

    def __str__(self):

        return f"Welcome {self.email}"

