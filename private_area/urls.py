from django.urls import path, include
from .views import PrivateArea


app_name = 'private_area'


urlpatterns = [
    path('',PrivateArea.as_view(), name='private_area')
]