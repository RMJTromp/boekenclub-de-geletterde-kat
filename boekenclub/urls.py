from django.urls import path, include

from boekenclub import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('register/', views.register, name='register'),
    path('manage-users/', views.manage_users_view, name='manage_users'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('delete_profile/<int:user_id>/', views.delete_profile_view, name='delete_profile'),
    path('delete_read/<int:read_id>/', views.delete_read_view, name='delete_read'),
]