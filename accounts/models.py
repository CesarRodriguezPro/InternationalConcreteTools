from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f"@{self.username}"