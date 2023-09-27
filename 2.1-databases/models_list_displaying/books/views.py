from datetime import datetime as dt
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from . import models

ALL_BOOKS = models.Book.objects.all()
SORTED_BOOKS = models.Book.objects.all().order_by('pub_date')

def index(request):
    return redirect('books/')

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': ALL_BOOKS}
    return render(request, template, context)

def book_date(request, pub):
    date_strings = [book.pub_date.strftime('%Y-%m-%d') for book in SORTED_BOOKS]
    paginator = Paginator(date_strings, 1)
    page_obj = paginator.get_page(date_strings.index(pub)+1)
    context = {
        'home': reverse('books'),
        'page': page_obj,
        'book': models.Book.objects.get(pub_date=pub),
    }
    if page_obj.has_next():
        context |= {'next_page': paginator.get_page(date_strings.index(pub)+2).object_list[0]}
    if page_obj.has_previous():
        context |= {'prev_page': paginator.get_page(date_strings.index(pub)).object_list[0]}
    return render(request, 'books/book_date.html', context)