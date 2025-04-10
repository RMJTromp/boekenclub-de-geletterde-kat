from django.urls import path, include

from boekenclub import views

urlpatterns = [
    path('home/', views.home, name='home'),
]