from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Bar, Menu, Item, Drink

def index(request):
    bar_list = Bar.objects.order_by('id')

    context = {
        'bar_list': bar_list,
    }

    return render(request, 'bar/index.html', context)

def bar_page(request, bar_id):
    bar = get_object_or_404(Bar, pk=bar_id)
    menu = Menu.objects.get(bar=bar_id)
    items = Item.objects.filter(menu=menu.id)
    menuList = []

    for item in items:
        drink = Drink.objects.get(pk=item.drink.id)
        menuList.append({
        'name':drink.name,
        'price':item.price,
        'size': item.size,
        'location': drink.location,
        'total_amount': item.total_amount,
        'current_amount' : item.current_ammount,
        })

    response = "You're looking at bar %s."

    context = {
        'bar': bar,
        'menu': menu,
        'menuList': menuList,
    }

    return render(request, 'bar/bar_page.html', context)

def next(request, bar_id):
    return HttpResponse("You're looking at another page for %s." % bar_id)

def pos(request, bar_id):
    bar = get_object_or_404(Bar, pk=bar_id)

    context = {
        'bar': bar,
    }

    return render(request, 'bar/pos.html', context)
