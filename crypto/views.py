from django.shortcuts import render,redirect
import coinbase
from coinbase.wallet.client import Client
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from . forms import MyUserCreationForm
from decouple import config


client = Client(config('api_key'),config('api_secret_key'))
# Create your views here.
class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    rates = client.get_exchange_rates(currency='BTC')
    rates2 = client.get_exchange_rates(currency='ETH')
    rates3 = client.get_exchange_rates(currency='XRP')
    time = dict(client.get_time())
    context = {"rates":rates["rates"]["USD"],"rates2":rates2["rates"]["USD"],
    "rates3":rates3['rates']['USD'], "time":repr(time['iso']), "naira":rates["rates"]["NGN"],
    "naira2":rates2['rates']['NGN'],"naira3":rates3['rates']['NGN']}
    return render(request, "base.html",context)

def index(request):
    return render(request,"registration/login.html")
