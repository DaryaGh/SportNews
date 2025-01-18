from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('a new user registered')
#         else:
#             return HttpResponse('invalid form')
#     else:
#         form = UserCreationForm()
#         return render (request,'register.html',{'form':form})

def auth_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return HttpResponseRedirect(reverse('auth_login'))

    form = CustomUserCreationForm()
    return render(request, 'register.html' , {'form':form})

def auth_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            # print(user_name, password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("News_list"))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html' , {'form':form})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("auth_login"))