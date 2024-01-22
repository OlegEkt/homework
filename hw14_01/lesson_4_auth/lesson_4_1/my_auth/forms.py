from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Record

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'password1', 'password2')

class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(widget=forms.DateInput)


    class Meta:
        model = Profile
        fields = ('birthday', 'tel')


class RecordForm(forms.ModelForm):


    class Meta:
        model =Record
        exclude = ('user',)



class ImagesForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': 'multiple'}), required=False)