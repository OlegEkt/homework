from django.shortcuts import render, redirect
from django.http import HttpResponse


def index_page(request, *args, **kwargs):
    return render(request, 'app_top/index.html')

def writers_page(request, *args, **kwargs):
    return render(request, 'app_top/writers.html')

def books_page(request, *args, **kwargs):
    return render(request, 'app_top/books.html')


top_books = [
    (1, 'Iron Flame'),
    (2, 'The Woman In Me'),
    (3, 'Fourth Wing (Special Edition)'),
]

def book_detail(request, position):
    position = int(position)

    if position <= len(top_books):
        book_id, book_title = top_books[position - 1]
        context = {
            'book_id': book_id,
            'book_title': book_title,
        }
        return render(request, 'app_top/book_detail.html', context)
    else:
        return redirect('books_page')
