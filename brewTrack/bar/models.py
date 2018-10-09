from django.db import models
import datetime

# Create your models here.

# bar model
# location (addresses string)
# menu (list)
# hours
# cover price (int list)
# weekly calendar list (list)****
# specials (list)
# admin list
# tab list (list (string))
# transcation list
class Bar(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    location = models.CharField(max_length=100, default='unknown')
    hours = models.CharField(max_length=50, default='unknown')

# Drink Model
class Drink(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    alcholic = models.BooleanField(default=True)
    ingridents = models.CharField(max_length=500, default='unknown') # Possibly make this its own model eventually
    alcholic_content = models.CharField(max_length=100, default='unknown')
    location = models.CharField(max_length=30, default='unknown')
    type = models.CharField(max_length=20, default='unknown')


#Menu Model
class Menu(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    #Many to Many with drinks


# Event model
class Event(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    type = models.CharField(max_length=20, default='unknown')
    description = models.CharField(max_length=100, default='unknown')
    date = models.DateTimeField('date published')
    ticket = models.BooleanField(default=False)

# user model
# username
# password
# admin list
class User(models.Model):
    name = models.CharField(max_length=20, default='unknown')
