from django.shortcuts import render
from django.http import HttpResponse

def index_page(request, *args, **kwargs):
    return render(request, 'app_city/index.html')

def news_page(request, *args, **kwargs):
    return render(request, 'app_city/news.html')

def management_page(request, *args, **kwargs):
    return render(request, 'app_city/management.html')

def history_page(request, *args, **kwargs):
    return render(request, 'app_city/history.html')

def contacts_page(request, *args, **kwargs):
    return render(request, 'app_city/contacts.html')