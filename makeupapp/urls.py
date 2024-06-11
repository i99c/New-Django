from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('cilt/', cilt, name='cilt'),
    path('login/', login, name='login'),
    path('register/', register, name='register.html'),
]
