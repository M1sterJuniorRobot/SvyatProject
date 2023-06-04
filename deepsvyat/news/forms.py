from .models import Articles
from django import forms
from django.shortcuts import render, redirect
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class ArticlesForm(ModelForm):
    title = forms.CharField(max_length=50,
                            required=True,
                            widget=TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Название статьи',
                                                    }))
    anons = forms.CharField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Анонс статьи'
                                                          }))
    # date = forms.DateTimeField(widget=DateTimeInput(attrs={'class': 'form-control',
    #                                                        'placeholder': 'Введите дату'}))
    full_text = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.Textarea(attrs={'class': 'form-control',
                                                             'placeholder': 'Текст статьи'
                                                             }))

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']
