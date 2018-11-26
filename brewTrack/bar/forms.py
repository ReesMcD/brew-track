from django.contrib.auth.models import User
from .models import *
from django import forms

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'uk-input text-input','placeholder' : 'username',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'uk-input text-input','placeholder' : 'email',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'uk-input text-input','placeholder' : 'password',}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'uk-input text-input','placeholder' : 'username',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'uk-input text-input','placeholder' : 'password',}))

    class Meta:
        model = User
        fields = ['username', 'password']


class BarPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['total_amount'].label = "Keg Size (oz)"
          self.fields['size'].label = "Size (oz)"
          self.fields['amount_flag'].label = "Is There A Keg?"

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'uk-input text-input','placeholder' : 'Bud Light, Vodka Cranberry, Yuengling Lager, ...',}))
    size = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'uk-input text-input','placeholder' : '12, 16, 24, ...',}))
    price = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'uk-input text-input','placeholder' : 'Price of Drink ($)',}))
    type = forms.ChoiceField(choices=[('Beer','Beer'),('Cocktail','Cocktail'),('Wine','Wine')], widget=forms.Select(attrs={'class':'uk-input text-input',}))
    subtype = forms.CharField(widget=forms.TextInput(attrs={'class': 'uk-input text-input','placeholder' : 'IPA, Vodka, Lager, Whiskey, ...',}))
    amount_flag = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'uk-checkbox text-check',}))
    total_amount = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'uk-input text-input','placeholder' : 'Total ounces of the keg (generally 1980 oz.)'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'uk-input text-input','placeholder' : 'Philadelphia PA, Athens GA, ...',}))
    alcholic_content = forms.DecimalField(required=False, max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'uk-input text-input','placeholder' : 'ABV',}))

    class Meta:
        model = Item
        fields = ['name', 'size', 'price', 'type', 'subtype', 'amount_flag', 'total_amount', 'location', 'alcholic_content']
