from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, TemplateView, ListView
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from bar.forms import *
from .models import *

class Index(ListView):
    model = Bar
    template_name = 'bar/index.html'

def logout_view(request):
    logout(request)
    return redirect('/')

class BarPage(DetailView):
    model = Bar
    slug_field = 'pk'
    template_name = 'bar/bar_page.html'

    def get_context_data(self, **kwargs):
       context = super(BarPage, self).get_context_data(**kwargs)
       menu = Menu.objects.get(bar=self.get_object())
       menuList = []
       typeList = {}
       items = Item.objects.filter(menu=menu.id)

       for item in items:
           drink = Drink.objects.get(pk=item.drink.id)
           menuList.append({
           'name':drink.name,
           'price':item.price,
           'size': item.size,
           'location': drink.location,
           'total_amount': item.total_amount,
           'current_amount' : item.current_ammount,
           'type' : drink.type,
           })

           if drink.type not in typeList:
               typeList[drink.type] = drink.type

    # Orders menuList alphabetically
       orderedMenuList = sorted(menuList, key=lambda k: k['name'])
       context['menu'] = menu
       context['menuList'] = orderedMenuList
       context['typeList'] = typeList
       return context

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
    # form_class = LoginForm()
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
