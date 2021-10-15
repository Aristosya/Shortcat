from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', views.registration, name="registration"),
    path('authorization', auth_views.LoginView.as_view(template_name='registration/user.html'), name="authorization"),
    path('authorization_exit', auth_views.LogoutView.as_view(template_name='registration/exit.html'), name="authorization_exit"),
    path('profile', views.profile, name="profile"),
]