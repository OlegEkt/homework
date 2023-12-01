from django.urls import path
from .views import index_page, news_page, management_page, history_page, contacts_page




urlpatterns = [

    path('', index_page, name='index_page'),
    path('news/', news_page, name='news_page'),
    path('management/', management_page, name='management_page'),
    path('history/', history_page, name='history_page'),
    path('contacts/', contacts_page, name='contacts_page'),

]