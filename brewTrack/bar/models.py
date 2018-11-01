from django.db import models
import datetime

# Bar Model
class Bar(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    location = models.CharField(max_length=100, default='unknown')
    hours = models.CharField(max_length=50, default='unknown')

#Menu Model
class Menu(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True)

# Drink Model
class Drink(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    alcholic = models.BooleanField(default=True)
    ingridents = models.CharField(max_length=500, default='unknown', null=True) # Possibly make this its own model eventually
    alcholic_content = models.CharField(max_length=100, default='unknown', null=True)
    location = models.CharField(max_length=30, default='unknown', null=True)
    type = models.CharField(max_length=20, default='unknown')

#Item Model
class Item(models.Model):
    price = models.DecimalField(decimal_places=2,max_digits=3)
    size = models.IntegerField()
    total_amount = models.IntegerField(null=True)
    current_ammount = models.IntegerField(null=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

#Event model
class Event(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    type = models.CharField(max_length=20, default='unknown')
    description = models.CharField(max_length=100, default='unknown')
    date = models.DateTimeField('date published')
    ticket = models.BooleanField(default=False)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True)

# user model
# username
# password
# admin list
class User(models.Model):
    name = models.CharField(max_length=20, default='unknown')
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True)
