from django.shortcuts import render
from django.http import HttpResponse



top_auto = {
    'Toyota' : {'model': 'Camry', 'gear': 'auto', 'fuel': 'diesel', 'year': '2023'},
    'Honda' : {'model': 'Civic', 'gear': 'robot', 'fuel': 'gas', 'year': '2021'},
    'Renault' : {'model': 'Megan', 'gear': 'manual', 'fuel': 'electro', 'year': '2022'},
}

def index_page(request, *args, **kwargs):
    return render(request, 'app_auto/index.html')

def auto_detail(request, auto_title):
    if auto_title in top_auto:
        auto_info = top_auto[auto_title]

        context = {
            'auto_title': auto_title,
            'auto_info': auto_info,
        }
        return render(request, 'app_auto/auto_detail.html', context)