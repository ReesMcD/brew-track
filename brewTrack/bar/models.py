from django.db import models

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
    location = models.CharField(max_length=100)
    hours = models.CharField(max_length=50)

# Drink Model
class Drink(models.Model):
    name = models.CharField(max_length=20)
    alcholic = models.BooleanField(Defult=True)
    ingridents = models.CharField(max_length=500) # Possibly make this its own model eventually
    alcholic_content = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    

#Menu Model
class Menu(models.Model):
    name = models.CharField(max_length=20)
    #Many to Many with drinks


# Event model
class Event(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    date = models.DateTimeField()
    ticket = models.BooleanField(default=False)

# user model
# username
# password
# admin list
class User(models.Model):
    name = models.CharField(max_length=20)
