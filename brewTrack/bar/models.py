from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')



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


# drinks model
# name
# alcholic
# non alcoholic
# ingridents (optional)
# price (optional)
# alcohol content (optional)
# craft beer (location) (optional)
# type (subtype) (optional)


# event model
# name
# type
# description
# date
# ticket
# non ticket


# user model
# username
# password
# admin list
