from django.shortcuts import render
from django.shortcuts import HttpResponse

from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Главня',
        'content': 'Магазин мебели Home',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему магаз такой бомбовый',
    }
    return render(request, 'main/index.html', context)
