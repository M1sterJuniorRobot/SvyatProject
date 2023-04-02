from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('date')[:3]
    return render(request, 'news/news_home.html', {'news': news})


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class ProjectLoginView():
    template_name = 'login.html'
    # доделать


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}!')
        return redirect('news-home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
