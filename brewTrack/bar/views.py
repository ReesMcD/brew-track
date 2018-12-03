from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from bar.forms import *
from .models import *
import datetime
import json

class Index(ListView):
    model = Bar
    # Ordering Alphabetically
    ordering = ['name']
    template_name = 'bar/index.html'

# Kept this a Functinon based view for simplicity
def logout_view(request):
    logout(request)
    return redirect('/')

class Profile(ListView):
    model = Bar
    # Ordering Alphabetically
    ordering = ['name']
    template_name = 'bar/profile.html'

class CreateBarPage(CreateView):
    model = Bar
    form_class = BarForm
    template_name = 'bar/event_form.html'

    def form_valid(self, form):
        bar = form.save(commit=False)
        bar.pub_date = datetime.datetime.today().strftime('%Y-%m-%d')
        bar.save()
        menu = Menu.objects.create(name=bar.name + " Menu", bar=bar)

        # TODO: Change to redirct to last page
        return redirect('/')

class UpdateBarPage(UpdateView):
    model = Bar
    form_class = BarForm
    template_name = 'bar/event_form.html'

    def form_valid(self, form):
       form.save()
       # TODO: Change to redirct to last page
       return redirect('/')

class DeleteBarPage(DeleteView):
    model = Bar
    # TODO: Change to redirct to last pagef
    success_url = reverse_lazy('bar:index')

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
        events = Event.objects.filter(bar=pk).order_by('date')[:3]

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

# CRUD for Item
class CreateItemPage(CreateView):
    form_class = ItemForm
    template_name = 'bar/item_form.html'

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


class UpdateItemPage(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'bar/item_form.html'

    def form_valid(self, form):
       form.save()
       # TODO: Change to redirct to last page
       return redirect('/')

class DeleteItemPage(DeleteView):
    model = Item
    # TODO: Change to redirct to last pagef
    success_url = reverse_lazy('bar:index')

# CRUD Events
class CreateEventPage(CreateView):
    form_class = EventForm
    template_name = 'bar/event_form.html'

    def get_context_data(self, **kwargs):
       context = super(CreateEventPage, self).get_context_data(**kwargs)
       pk = self.kwargs['pk']
       bar = Bar.objects.get(pk=pk)
       context['bar'] = bar
       return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        bar = Bar.objects.get(pk=pk)
        event = form.save(commit=False)
        event.bar = bar
        event.save()
        return redirect('/bar/' + pk)


class EventPage(ListView):
    model = Bar
    # Ordering Alphabetically
    ordering = ['date']
    template_name = 'bar/events.html'

    def get_context_data(self, **kwargs):
       context = super(EventPage, self).get_context_data(**kwargs)
       pk = self.kwargs['pk']
       bar = Bar.objects.get(pk=pk)
       menu = Menu.objects.get(bar=pk)
       events = Event.objects.filter(bar=bar.id)

       context['events'] = events
       context['bar'] = bar
       return context

class UpdateEventPage(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'bar/event_form.html'

    def form_valid(self, form):
       form.save()
       # TODO: Change to redirct to last page
       return redirect('/')

class DeleteEventPage(DeleteView):
    model = Event
    # TODO: Change to redirct to last pagef
    success_url = reverse_lazy('bar:index')


class PointOfSales(View):
    model = Bar
    # form_class = PayForm
    template_name = 'bar/pos.html'

    def get(self, request, pk):

        # pk = self.kwargs['pk']
        bar = get_object_or_404(Bar, pk=pk)
        menu = Menu.objects.get(bar=pk)
        items = Item.objects.filter(menu=menu.id).order_by('name')

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
            'items' : items,
            'typeList' : typeList,
            'subList' : sorted(subList)
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        pk = self.kwargs['pk']
        bar = get_object_or_404(Bar, pk=pk)
        menu = Menu.objects.get(bar=pk)
        items = Item.objects.filter(menu=menu.id).order_by('name')

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
            'items' : items,
            'typeList' : typeList,
            'subList' : sorted(subList)
        }

        json_data=json.loads(request.body)

        try:
            for p_item in json_data:
                item = Item.objects.get(pk=p_item['id'])
                if item.current_amount:
                    current_amount = item.current_amount  - (item.size * p_item['count'])
                    Item.objects.filter(pk=p_item['id']).update(current_amount=current_amount)

                purchases = item.purchases + p_item['count']
                Item.objects.filter(pk=p_item['id']).update(purchases=purchases)

        except Exception as error:
            print('Caught this error: ' + repr(error))


        return render(request, self.template_name, context)


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
