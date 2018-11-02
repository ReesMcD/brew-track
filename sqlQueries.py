from bar.models import Bar, Menu, Drink, Item, Event, User
from django.utils import timezone

bar = Bar(name='Local Whisky', pub_date=timezone.now(), location="107 E Beaver Ave, State College, PA 16801", hours='5pm-2am')

p = Bar.objects.get(pk=3)

menu = Menu(name='Phryst Menu', bar=p)
