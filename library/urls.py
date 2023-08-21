"""
URL configuration for book_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    # Author paths
    path('api/authors/', views.all_authors, name='all_authors'),
    path('api/authors/add/', views.add_author, name='add_author'),
    path('api/authors/update/<int:author_id>/', views.update_author, name='update_author'),
    path('api/authors/delete/<int:author_id>/', views.delete_author, name='delete_author'),


    # Category paths
    path('api/categories/', views.all_categories, name='all_categories'),
    path('api/categories/add/', views.add_category, name='add_category'),
    path('api/categories/update/<int:category_id>/', views.update_category, name='update_category'),
    path('api/categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),


    # Book paths
    path('api/books/', views.all_books, name='all_books'),
    path('api/books/add/', views.add_book, name='add_book'),
    path('api/books/update/<int:book_id>/', views.update_book, name='update_book'),
    path('api/books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    
]
