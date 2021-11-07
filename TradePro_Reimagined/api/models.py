from django.db import models
import string
import random
# We want to have "fat" models and "thin" views


def generate_unique_code():
    """
    Generate random 6 length code
    """

    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code
        



class Room(models.Model):
    """
    This is basically the equivalent of a table in a database

    """
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
