from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username