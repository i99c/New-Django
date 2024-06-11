from django.shortcuts import render, redirect
from .models import *
from makeupapp.models import CartItem

# Create your views here.
def index(request):
    return render(request, 'index.html')


def cilt(request):
    return render(request, 'cilt.html')

def login(request):
    return render(request, 'login.html')