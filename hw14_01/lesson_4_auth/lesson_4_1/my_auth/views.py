from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.core.files import images
from django.shortcuts import render, redirect
from django.template import context
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views import View

from django.views.generic import DetailView #my

from .forms  import UserForm, ProfileForm, RecordForm, ImagesForm
from .models import Profile, Record, ImagesRecord
from django.contrib import messages



def main_page(request, *args, **kwargs):
    records = Record.objects.all()[:3]
    return render(request, 'my_auth/base.html', context={'records': records})


def login_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'my_auth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main')

    return render(request, 'my_auth/login.html', {'error': 'auth error'})


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('main')


def logout_view(request):
    logout(request)
    return redirect('main')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            birthday = profile_form.cleaned_data['birthday']
            tel = profile_form.cleaned_data['tel']
            Profile.objects.create(
                user=user,
                birthday=birthday,
                tel=tel
            )
            username = user_form.cleaned_data['username']
            raw_password = user_form.cleaned_data['password1']
            auth_user = authenticate(username=username, password=raw_password)
            login(request, auth_user)
            return redirect('main')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid fields')

    user_form = UserForm()
    profile_form = ProfileForm()
    return render(request, 'my_auth/register.html', context={
        'user_form': user_form,
        'profile_form': profile_form
    })


class RecordFormView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        record_form = RecordForm()
        image_form = ImagesForm()
        return render(request, template_name='my_auth/record_form.html',
                      context={'record_form': record_form, 'image_form': image_form})

    def post(self, request):
        record_form = RecordForm(request.POST)
        image_form = ImagesForm(request.POST, request.FILES)
        if record_form.is_valid() and image_form.is_valid():
            new_record = record_form.save(commit=False)
            new_record.user_id = request.user.profile.id
            new_record.save()
            images = request.FILES.getlist('image')
            for i_img in images:
                instance = ImagesRecord(image=i_img, record=new_record)
                instance.save()
            return redirect('main')
        return render(request, template_name='my_auth/record_form.html',
                      context={'record_form': record_form, 'image_form': image_form,
                               'error': 'Something went wrong'})


class RecordDetailView(DetailView):
    model = Record
    template_name = 'record_detail.html'
    context_object_name = 'record'