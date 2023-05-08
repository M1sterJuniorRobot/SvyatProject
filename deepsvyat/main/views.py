from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def test(request):
    return render(request, 'main/test.html')


def newspapper(request):
    return HttpResponse("<h4>Тут будут выводиться новости </h4>")
