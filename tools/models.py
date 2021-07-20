from django.db import models
from accounts.models import User
from locations.models import Locations


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tool(models.Model):
    code = models.CharField(max_length=225, unique=True)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True, blank=True )
    tags = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    current_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    current_location = models.ForeignKey(Locations, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type.name} | current user: {self.current_user} in {self.current_location} '


class TempImage(models.Model):
    image = models.ImageField(upload_to='temp_image/', blank=True, null=True)






