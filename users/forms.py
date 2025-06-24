from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.form import StyleFormMixin
from .models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   help_text='Необязательное поле. Введите ваш номер телефона.')
    username = forms.CharField(max_length=50, required=True, help_text='Псевдоним')
    country = forms.CharField(max_length=70, required=True, help_text='Страна проживания')

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'password1', 'password2',)
