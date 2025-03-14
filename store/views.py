from django.shortcuts import render

from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html')

def detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'detail.html', {'product': product})
from django.shortcuts import render

# Create your views here.
