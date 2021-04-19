from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ExtendedRegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=255, required=False)
    # last_name = forms.CharField(max_length=255, required=False)
    # email = forms.EmailField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
