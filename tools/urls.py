from django.urls import path
from .views import Home, CreateTool, CreateType


app_name = 'tools'


urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('create_tool',CreateTool.as_view(), name='create_tool'),
    path('create_type', CreateType.as_view(), name='create_type'),
]