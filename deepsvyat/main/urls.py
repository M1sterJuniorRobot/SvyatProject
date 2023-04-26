from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('test', views.test, name='test'),
    path('register/', user_views.register, name='register')
]
