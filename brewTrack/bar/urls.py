from django.conf.urls import url
from .views import *

from . import views

app_name = 'bar'
urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^register', Register.as_view(), name='register'),
    url(r'^login', Login.as_view(), name='login'),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^user/profile/$', Profile.as_view(), name='profile'),
    url(r'^bar/(?P<pk>[0-9]+)/$', BarPage.as_view(), name='bar'),
    url(r'^bar/create/$', CreateBarPage.as_view(), name='create_bar'),
    url(r'^bar/(?P<pk>[0-9]+)/edit_bar/$', UpdateBarPage.as_view(), name='update_bar'),
    url(r'^bar/(?P<pk>[0-9]+)/delete_bar/$', DeleteBarPage.as_view(), name='delete_bar'),

    # Item CRUD
    url(r'^bar/(?P<pk>[0-9]+)/create_item/$', CreateItemPage.as_view(), name='create_item'),
    url(r'^item/(?P<pk>[0-9]+)/edit_item/$', UpdateItemPage.as_view(), name='update_item'),
    url(r'^item/(?P<pk>[0-9]+)/delete_item/$', DeleteItemPage.as_view(), name='delete_item'),
    # Event CRUD
    url(r'^bar/(?P<pk>[0-9]+)/create_event/$', CreateEventPage.as_view(), name='create_event'),
    url(r'^event/(?P<pk>[0-9]+)/edit_event/$', UpdateEventPage.as_view(), name='update_event'),
    url(r'^event/(?P<pk>[0-9]+)/delete_event/$', DeleteEventPage.as_view(), name='delete_event'),
    url(r'^bar/(?P<pk>[0-9]+)/events/$', EventPage.as_view(), name='events'),

    url(r'^bar/(?P<pk>[0-9]+)/next/$', NextBarPage.as_view(), name='next'),
    url(r'^bar/(?P<pk>[0-9]+)/pos/$', PointOfSales.as_view(), name='pos'),
]
