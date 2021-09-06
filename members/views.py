from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    rgf = RegistrationForm()
    if request.method == 'POST':
        rgf = RegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    return render(request, 'registration/registration.html', {'rgf': rgf})


def loginuser(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')

