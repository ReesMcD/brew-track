from django.db import models
import datetime

# Bar Model
class Bar(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    location = models.CharField(max_length=100, default='')
    hours = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

#Menu Model
class Menu(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, default="%s Menu" % bar.name)

    def __str__(self):
        return self.name

#Item Model
class Item(models.Model):
    name = models.CharField(max_length=50, default='')
    size = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    type = models.CharField(max_length=20, default='')
    subtype = models.CharField(max_length=20, default='')
    amount_flag = models.BooleanField(default=True)
    purchases = models.IntegerField(default=0)
    ingridents = models.CharField(max_length=500, blank=True, default='')
    location = models.CharField(max_length=30, blank=True, null=True)
    total_amount = models.IntegerField(null=True, blank=True)
    current_amount = models.IntegerField(null=True, blank=True)
    alcholic_content = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('bar:bar', kwargs={'pk': self.pk})

    def __str__(self):
        return self.menu.name + " - " + self.name

#Event model
class Event(models.Model):
    name = models.CharField(max_length=20, default='')
    type = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='', blank=True)
    date = models.CharField('Event Date', max_length=20, default='')
    frequancy = models.CharField('Frequancy', max_length=500, default='', blank=True)
    ticket = models.BooleanField(default=False)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.bar.name + " - " + self.name
