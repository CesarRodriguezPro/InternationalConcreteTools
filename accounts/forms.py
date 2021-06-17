from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2','is_admin')
        model = User
