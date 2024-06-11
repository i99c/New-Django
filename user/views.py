from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django import forms


# Create your views here.
def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kayıt Başarıyla Tamamlandı')
            return redirect('login')

    context = {
        'form' : form
    }

    return render(request, 'register.html', context)

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput)

def userLogin(request):

    if request.method == "POST":
        form = LoginForm(request.POST)  # LoginForm, kullanıcı girişi için kullanacağınız form sınıfınızın adı
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None: 
                login(request, user)
                messages.success(request, 'Başarıyla Giriş Yapıldı')
                return redirect('index')
            else:
                messages.error(request, 'Kullanıcı Adı veya Şifre Yanlış')
                return redirect('login')
    else:
        form = LoginForm()  # LoginForm, kullanıcı girişi için kullanacağınız form sınıfınızın adı

    return render(request, "login.html", {'form': form})
