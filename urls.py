from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import SignupView


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'accounts/logged_out.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'accounts/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html')),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html')),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html')),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('signup/', SignupView.as_view(), name = 'signup'),
    path('', TemplateView.as_view(template_name = 'accounts/index.html'), name = 'index'),
]