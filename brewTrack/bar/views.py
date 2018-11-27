from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, TemplateView, ListView
from django.template import loader
# from django.contrib.gis.utils import GeoIP
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
class BarPage(TemplateView):
    template_name = 'bar/bar_page.html'
    slug_field = 'pk'

    def get(self, request, pk):
        form = BarPageForm()
        bar = get_object_or_404(Bar, pk=pk)
        menu = Menu.objects.get(bar=pk)
        typeList = {}
        subList = {}
        items = Item.objects.filter(menu=menu.id).order_by('name')
        events = Event.objects.filter(bar=pk).order_by('date')



        for item in items:
          if item.type not in typeList:
              typeList[item.type] = item.type

          if item.subtype not in subList:
             subList[item.subtype] = item.subtype

        context = {
            'form' : form,
            'bar' : bar,
            'menu' : menu,
            'events': events,
            'menuList' : items,
            'typeList' : typeList,
            'subList' : sorted(subList)
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = BarPageForm(request.POST)
        bar = get_object_or_404(Bar, pk=pk)
        menu = Menu.objects.get(bar=pk)

        if form.is_valid():
            item = form.save(commit=False)
            item.current_amount = item.total_amount
            item.menu = menu
            item.save()
            return redirect('/bar/' + pk)

        return render(request, self.template_name, {'form' : form})

# This is a Test Page
class NextBarPage(DetailView):
    model = Bar
    slug_field = 'pk'
    template_name = 'bar/next.html'

    def get_context_data(self, **kwargs):
       context = super(NextBarPage, self).get_context_data(**kwargs)
       return context

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
