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
    path('book/create', views.book_create, name='book_create'),
    path('books', views.books_list, name='book_list'),
    path('books/review', views.books_review, name='books_review'),
    path('books/review/accept/<int:pk>', views.book_accept, name='book_accept'),
    path('book/<int:pk>/delete', views.book_delete, name='book_delete'),
    path('book/<int:pk>/edit', views.book_edit, name='book_edit'),
]