from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from bar.forms import *
from .models import *
import logging

logger = logging.getLogger(__name__)

class Index(ListView):
    model = Bar
    # Ordering Alphabetically
    ordering = ['name']
    template_name = 'bar/index.html'

# Kept this a Functinon based view for simplicity
def logout_view(request):
    logout(request)
    return redirect('/')

# Bar Page and Form
class BarPage(DetailView):
    template_name = 'bar/bar_page.html'
    model = Bar

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(BarPage, self).get_context_data(**kwargs)
        bar = get_object_or_404(Bar, pk=pk)
        menu = Menu.objects.get(bar=pk)
        items = Item.objects.filter(menu=menu.id).order_by('name')
        events = Event.objects.filter(bar=pk).order_by('date')

        typeList = {}
        subList = {}
        for item in items:
          if item.type not in typeList:
              typeList[item.type] = item.type
          if item.subtype not in subList:
             subList[item.subtype] = item.subtype

        context = {
            'bar' : bar,
            'menu' : menu,
            'events': events,
            'menuList' : items,
            'typeList' : typeList,
            'subList' : sorted(subList)
        }

        return context


class CreateItemPage(CreateView):
    form_class = ItemForm
    template_name = 'bar/create_item_form.html'

    def get_context_data(self, **kwargs):
       context = super(CreateItemPage, self).get_context_data(**kwargs)
       pk = self.kwargs['pk']
       bar = Bar.objects.get(pk=pk)
       menu = Menu.objects.get(bar=pk)
       context['bar'] = bar
       context['menu'] = menu
       return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        menu = Menu.objects.get(bar=pk)
        item = form.save(commit=False)
        item.current_amount = item.total_amount
        item.menu = menu
        item.save()
        return redirect('/bar/' + pk)

# Cant save but init view works
class UpdateItemPage(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'bar/create_item_form.html'

    def form_valid(self, form):
       form.save()
       # Change to redirct to last page
       return redirect('/')


class PointOfSales(DetailView):
    model = Bar
    slug_field = 'pk'
    template_name = 'bar/pos.html'

    def get_context_data(self, **kwargs):
       context = super(PointOfSales, self).get_context_data(**kwargs)
       return context

class Login(TemplateView):
    template_name = 'bar/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form' : form})

class Register(TemplateView):
    template_name = 'bar/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form' : form})

# This is a Test Page
class NextBarPage(DetailView):
    model = Bar
    template_name = 'bar/next.html'

    def get_context_data(self, **kwargs):
       context = super(NextBarPage, self).get_context_data(**kwargs)
       return context
