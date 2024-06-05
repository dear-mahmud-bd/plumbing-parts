from django.shortcuts import render
from store.models import Product

def home(req):
    products = Product.objects.all()
    return render(req, 'home.html', {'products':products})
