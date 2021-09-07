from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# extending Django's UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # specify the model that the form will interact with
    # class Meta, a nested namespace for configurations
    class Meta:
        model = User
        # fields that will be shown on the form and in what order
        fields = ['username', 'email', 'password1', 'password2']

# inherits from ModelForm
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # specify the model that the form will interact with
    # class Meta, a nested namespace for configurations
    class Meta:
        model = User
        # fields that will be shown on the form and in what order
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']