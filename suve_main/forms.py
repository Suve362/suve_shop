from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible
import re
from .models import Login


@deconstructible
class PasswordValidator:
    ALLOWED_CHARS = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-~_!@#$%^&*')
    code = 'password'

    def __init__(self, message=None):
        self.message = message if message else 'Minimum of 8 characters, latin letters, numbers, special characters(#,$,@,&)'

    def __call__(self, value,  *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)) and len(value) <= 8:
            raise ValidationError(self.message, code=self.code)


class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'field__input'}))
    password = forms.CharField(max_length=255,
                               widget=forms.PasswordInput(attrs={'class': 'field__input'}),
                               validators=[
                                   PasswordValidator(),
                               ])

    class Meta:
        model = Login
        fields = ['email', 'password']
        widgets = {
        }
        labels = {'email': 'Email',
                  'password': 'Password'}

    def clean_email(self):
        pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        email = self.cleaned_data['email']
        if re.search(pattern, email) is None:
            raise ValidationError("Invalid email")

        return email
