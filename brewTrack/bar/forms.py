from django.contrib.auth.models import User
from .models import *
from django import forms

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'uk-input','placeholder' : 'username',}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'uk-input','placeholder' : 'email',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'uk-input','placeholder' : 'password',}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'uk-input ','placeholder' : 'username',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'uk-input ','placeholder' : 'password',}))

    class Meta:
        model = User
        fields = ['username', 'password']

class BarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['location'].label = "Address"

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Name of Bar',}))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Full Address',}))
    hours = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Ex. 5pm-2am',}))

    class Meta:
        model = Bar
        fields = ['name', 'location', 'hours']


class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['total_amount'].label = "Keg Size (oz)"
          self.fields['size'].label = "Size (oz)"
          self.fields['amount_flag'].label = "Is There A Keg?"
          self.fields['location'].label = "Brewery Locaion"

    name = forms.CharField(widget=forms.TextInput(attrs={
        'id':'drink-name','class': 'uk-input ','placeholder' : 'Bud Light, Vodka Cranberry, Yuengling Lager, ...',}))
    size = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'uk-input ','placeholder' : '12, 16, 24, ...',}))
    price = forms.DecimalField(
        max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': 'uk-input ','placeholder' : 'Price of Drink ($)',}))
    type = forms.ChoiceField(
        choices=[('Beer','Beer'),('Cocktail','Cocktail'),('Wine','Wine')], widget=forms.Select(attrs={
        'id':'type-value','class':'uk-select',}))
    subtype = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'IPA, Vodka, Lager, Whiskey, ...',}))
    amount_flag = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={
        'class': 'uk-checkbox text-check',}))
    total_amount = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'uk-input ','placeholder' : 'Total ounces of the keg (generally 1980 oz.)'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Philadelphia PA, Athens GA, ...',}))
    alcholic_content = forms.DecimalField(
        required=False, max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={
        'class': 'uk-input ','placeholder' : 'ABV',}))

    class Meta:
        model = Item
        fields = ['name', 'size', 'price', 'type', 'subtype', 'amount_flag', 'total_amount', 'location', 'alcholic_content']

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Name of Event',}))
    type = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Band, Preformance, Special, etc.',}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Band, Preformance, Special, etc.',}))
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id':'datepicker','class': 'uk-input','type':"text",'placeholder' : 'Event Date',}))
    reoccuring_flag = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={
        'class': 'uk-checkbox text-check',}))
    frequancy = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'uk-input ','placeholder' : 'Sample: M 9pm-10pm, Th 10pm-2am',}))
    ticket_flag = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={
        'class': 'uk-checkbox text-check',}))

    class Meta:
        model = Event
        fields = ['name', 'type', 'description', 'reoccuring_flag', 'frequancy', 'ticket_flag', 'date']

class PayForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)

    class Meta:
        model = Item
        fields = ['current_amount', 'purchases']
