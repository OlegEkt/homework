from django.urls import path
from .views import index_page, auto_detail
from . import views


urlpatterns = [

         path('', index_page, name='index_page'),
         path('<str:auto_title>/', views.auto_detail, name='auto_detail')
    ]
