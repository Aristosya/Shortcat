from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('contacts', views.contacts, name='contacts'),
    path('link/', views.dashboard, name="link"),
    path('generate/', views.generate, name="generate"),
    path('deleteurl/', views.deleteurl, name="deleteurl"),
    path('<str:query>/', views.redirecttoshort, name="redirecttoshort"),
]