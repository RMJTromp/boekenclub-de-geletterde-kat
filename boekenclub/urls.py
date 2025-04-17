from django.urls import path, include

from boekenclub import views

urlpatterns = [
    path('', views.home, name='home'),
]