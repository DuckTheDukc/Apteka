from django.shortcuts import render


def login(request):
    context = {
        "title": "apteka - авторизация",
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
