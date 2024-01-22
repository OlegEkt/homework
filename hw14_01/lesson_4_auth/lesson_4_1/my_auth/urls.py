from django.conf.urls.static import static
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import main_page, login_view, logout_view, MyLogoutView, register_view, RecordFormView, RecordDetailView
from django.conf import settings



urlpatterns =[
    path('', main_page, name='main'),
    # path('login', login_view, name='login'),
    path('login/', LoginView.as_view(template_name='my_auth/login.html',
     redirect_authenticated_user=True), name='login'),
    path('logout', MyLogoutView.as_view(), name='logout'),
    path('register', register_view, name='register'),
    path('record_create/', RecordFormView.as_view(), name='record_create'),

    path('record/<int:pk>/', RecordDetailView.as_view(), name='record_detail')


    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)