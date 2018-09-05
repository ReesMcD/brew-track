from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, What bar could you like?")

def bar(request, bar_id):
    response = "You're looking at bar %s."
    return HttpResponse(response % bar_id)

def next(request, bar_id):
    return HttpResponse("You're look at another page for %s." % bar_id)
