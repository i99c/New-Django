from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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



def userLogin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None: 
            login(request,user)
            messages.success(request, 'Başarıyla Giriş Yapıldı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı Adı veya Şifre Yanlış')
            return redirect('login')

    return render(request, "login.html")
