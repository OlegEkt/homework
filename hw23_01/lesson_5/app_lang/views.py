from django.shortcuts import render
from .models import Book
# from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext


# Create your views here.

def books_list(request, *arg, **kwargs):
    books = Book.objects.all()
    count = len(books)
    books_num = ngettext(
        'here is %(count)d book',
        'here are %(count)d books',
        count,
    ) % {
        'count': count
    }
    # page_title = gettext('Books')
    page_title = _ ('Books')
    return render(request, 'app_lang/index.html', context={'books': books,
                                                           'page_title': page_title,
                                                           'books_num': books_num})
