from django.contrib import admin
from django.urls import path

from books.views import *

urlpatterns = [
    path('', index), 
    path('books/', books_view, name='books'),
    path('book/<pub>/', book_date, name='book_date'),
    path('admin/', admin.site.urls),
]
