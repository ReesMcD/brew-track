from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
