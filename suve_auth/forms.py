from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class PasswordValidator:
    ALLOWED_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-~_!@#$%^&*')
    code = 'password'

    def __init__(self, message=None):
        self.message = message if message else 'Minimum of 8 characters, latin letters, numbers, special characters(#,$,@,&)'

    def __call__(self, value,  *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)) and len(value) <= 8:
            raise ValidationError(self.message, code=self.code)


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'field__input'}),
        label="E-mail",
        error_messages={'invalid': 'Enter a valid email address.'}
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'field__input'}),
        validators=[
            PasswordValidator(),
        ],
    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise ValidationError(
                    "Please enter a correct email and password. Note that both fields may be case-sensitive.")
            elif not self.user_cache.is_active:
                raise ValidationError("This account is inactive.")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def clean_username(self):
        email = self.cleaned_data.get('username')
        pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if not re.search(pattern, email):
            raise ValidationError("Invalid email")
        return email

    class Meta:

        model = get_user_model()
        fields = ['email', 'password']
        # widgets = {
        #         }
        # labels = {'username': 'Email',
        #           'password': 'Password'}


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'field__input'}))
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'field__input'}))
    password1 = forms.CharField(label='Password', widget=(forms.PasswordInput(attrs={'class': 'field__input'})))
    password2 = forms.CharField(label='Confirm password', widget=(forms.PasswordInput(attrs={'class': 'field__input'})))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        # labels = {
        # }
        # widget = {
        # }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email):
            raise ValidationError('That username is taken. Try another.')
        return email
