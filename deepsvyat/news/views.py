from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('date')[:3] # запомни нахуй, эти :3 означают сколько выводить на страницу
    return render(request, 'news/news_home.html', {'news': news})


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.date = datetime.datetime.today()
            news.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
