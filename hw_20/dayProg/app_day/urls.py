from django.urls import path
from .views import programmers_day

urlpatterns = [

    path('', programmers_day, name='day')

]