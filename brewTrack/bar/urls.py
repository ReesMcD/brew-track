from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<bar_id>[0-9]+)/$', views.bar, name='bar'),
    # ex: /polls/5/results/
    url(r'^(?P<bar_id>[0-9]+)/next/$', views.next, name='bar'),
]
