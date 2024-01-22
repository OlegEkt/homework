from django.urls import path
from .views import books_list


urlpatterns = [
    path('', books_list, name='books')
]