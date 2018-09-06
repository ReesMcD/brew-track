from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Bar

def index(request):
    bar_list = Bar.objects.order_by('id')
    template = loader.get_template('bar/index.html')
    context = {
        'bar_list': bar_list,
    }
    return HttpResponse(template.render(context, request))

def bar(request, bar_id):
    response = "You're looking at bar %s."
    return HttpResponse(response % bar_id)

def next(request, bar_id):
    return HttpResponse("You're look at another page for %s." % bar_id)
