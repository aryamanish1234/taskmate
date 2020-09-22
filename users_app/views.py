from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Customregisterform
from django.contrib import messages
from todolist import views
# Create your views

# Create Authincation


def register(request):
    if request.method == "POST":
        register_form = Customregisterform(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("Your Account is Create go on login"))

            return redirect('register')

    else:
        register_form = Customregisterform()
    return render(request, 'users_app/register.html', {'register_form': register_form})
