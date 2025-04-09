from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        }

    # username = forms.CharField(
    #     label="имя",
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Введите имя пользователя",
    #         }
    #     ),
    # )
    # password = forms.CharField(
    #     label="пароль",
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autofocomlete": "current_password",
    #             "class": "form-control",
    #             "placeholder": "Введите пароль",
    #         }
    #     ),
    # )
