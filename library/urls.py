from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/update/<int:pk>/', views.author_update, name='author_update'),
    path('authors/delete/<int:pk>/', views.author_delete, name='author_delete'),
    # Add similar paths for Books and Borrowers
     path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),

    # Borrower URLs
    path('borrowers/', views.borrower_list, name='borrower_list'),
    path('borrowers/create/', views.borrower_create, name='borrower_create'),
    path('borrowers/update/<int:pk>/', views.borrower_update, name='borrower_update'),
    path('borrowers/delete/<int:pk>/', views.borrower_delete, name='borrower_delete'),
]
