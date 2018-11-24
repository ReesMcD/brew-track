from django.conf.urls import url
from .views import *

from . import views

app_name = 'bar'
urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^bar/(?P<pk>[0-9]+)/$', BarPage.as_view(), name='bar'),
    url(r'^bar/(?P<pk>[0-9]+)/next/$', NextBarPage.as_view(), name='next'),
    url(r'^bar/(?P<pk>[0-9]+)/pos/$', PointOfSales.as_view(), name='pos'),
    url(r'^register', Register.as_view(), name='Register'),
]
