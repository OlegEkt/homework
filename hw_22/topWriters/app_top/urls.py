from django.urls import path
from .views import index_page, index_page, writers_page, books_page, book_detail
from . import views



urlpatterns = [

    path('', index_page, name='index_page'),
    path('writers/', writers_page, name='writers_page'),
    path('books/', books_page, name='books_page'),
    path('books/<int:position>/', views.book_detail, name='book_detail'),

]