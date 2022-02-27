from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrationForm, SignInForm


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, "my_auth/base.html")


def registration(request, *args, **kwargs):
    if request.method == "GET":
        reg_form = RegistrationForm()
        return render(request, "my_auth/registration.html", context={"form": reg_form})

    elif request.method == "POST":
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            return redirect("login")
        else:
            return render(request, "my_auth/registration.html", context={"form": user_form})


def login(request, *args, **kwargs):
    if request.method == "GET":
        sign_in_form = SignInForm()
        return render(request, "my_auth/login.html", context={"form": sign_in_form})

    elif request.method == "POST":
        user_form = SignInForm(request.POST)

        if user_form.is_valid():
            return redirect("main")
        else:
            return render(request, "my_auth/login.html", context={"form": user_form})


def logout(request, *args, **kwargs):
    return redirect("login")


def main(request, *args, **kwargs):
    return render(request, "my_auth/home.html")
