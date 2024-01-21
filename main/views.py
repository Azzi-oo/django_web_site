from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return render(request, )


def about(request):
    return HttpResponse('Home page')