from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.froms import UserLoginForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
        "title": "apteka - авторизация",
        "form": form,
    }

    return render(
        request,
        "users/login.html",
        context,
    )


def registration(request):
    context = {
        "title": "apteka - регистрация",
    }
    return render(
        request,
        "users/registration.html",
        context,
    )


def profile(request):
    context = {
        "title": "apteka - кабинет",
    }
    return render(
        request,
        "users/profile.html",
        context,
    )


def logout(request): ...
