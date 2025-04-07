from django.shortcuts import render
from products.models import Categories


def index(request):
    categories = Categories.objects.all
    context = {
        "title": "apteka",
        "content": "главная страница аптеки",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "apteka-о нас", "content": "о нас", "text_on_page": "аптека во"}

    return render(request, "main/about.html", context)
