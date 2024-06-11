from django.shortcuts import render, redirect
from .models import *
from .models import Product
from makeupapp.models import CartItem

# Create your views here.
def index(request):
    return render(request, 'index.html')


def cilt(request):
    # Veritabanından 'Cilt Ürünleri' kategorisindeki ürünleri al
    cilt_urunler = Product.objects.filter(category__name='Cilt Ürünleri')
    
    return render(request, 'cilt.html', {'products': cilt_urunler})



def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')