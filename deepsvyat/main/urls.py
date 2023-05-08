from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('test', views.test, name='test'),
    path('w_users/', include('w_users.urls')),

]
