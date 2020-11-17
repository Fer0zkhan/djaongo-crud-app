from django.urls import path
from .views import *

urlpatterns = [
    path('books/home/', home, name='books_home'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit', edit_book, name='edit_book'),
    path('books/<int:pk>/delete', delete_book, name='delete_book')
]
