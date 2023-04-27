"""deepsvyat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Add the following to the list of previous imports
from django.contrib.auth import views as auth_views
from w_users.views import CustomLoginView
from w_users.forms import LoginForm

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('news/', include('news.urls')),
                  path('w_users/', include('w_users.urls')),
                  path('login/',
                       CustomLoginView.as_view(redirect_authenticated_user=True, template_name='w_users/login.html',
                                               authentication_form=LoginForm), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='w_users/logout.html'), name='logout'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
