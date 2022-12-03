from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def newspapper(request):
    return HttpResponse("<h4>Тут будут выводиться новости </h4>")


def test(request):
    return render(request, 'main/test.html')
