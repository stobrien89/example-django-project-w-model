# The Model class we will inherit from
from django.db import models

# new model class


class Turtle(models.Model):
    # define a string filed of max 100 characters
    name = models.CharField(max_length=100)
    # define an age that is an integer
    age = models.IntegerField
