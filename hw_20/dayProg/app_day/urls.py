from django.urls import path
from .views import day

urlpatterns = [

    path('', day, name='day')

]