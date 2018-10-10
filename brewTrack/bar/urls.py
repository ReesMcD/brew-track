from django.conf.urls import url

from . import views

app_name = 'bar'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bar/(?P<bar_id>[0-9]+)/$', views.bar_page, name='bar'),
    url(r'^(?P<bar_id>[0-9]+)/next/$', views.next, name='next'),
]
