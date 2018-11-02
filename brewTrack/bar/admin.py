from django.contrib import admin

from .models import Bar, Menu, Item, Drink, Event, User

admin.site.register(Bar)
admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Drink)
admin.site.register(Event)
admin.site.register(User)
# Register your models here.
