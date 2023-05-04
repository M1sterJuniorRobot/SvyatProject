from django.contrib.auth import views as auth_views
from w_users.views import CustomLoginView
from w_users.forms import LoginForm

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from w_users.views import ResetPasswordView


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('news/', include('news.urls')),
                  path('w_users/', include('w_users.urls')),

                  # url on sign in
                  path('login/',
                       CustomLoginView.as_view(redirect_authenticated_user=True, template_name='w_users/login.html',
                                               authentication_form=LoginForm), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='w_users/logout.html'), name='logout'),

                  # reset password url
                  path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
                  path('password-reset-confirm/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name='w_users/password_reset_confirm.html'),
                       name='password_reset_confirm'),

                  # confirm password reset
                  path('password-reset-complete/',
                       auth_views.PasswordResetCompleteView.as_view(template_name='w_users/password_reset_complete.html'),
                       name='password_reset_complete')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
