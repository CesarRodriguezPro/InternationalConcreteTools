from django.urls import path
from .views import Home, CreateTool, CreateType, ListViewType, DeleteType, UpdateType


app_name = 'tools'


urlpatterns = [
    #  basic Tools
    path('',Home.as_view(), name='home'),
    path('create_tool',CreateTool.as_view(), name='create_tool'),

    # for types
    path('create_type', CreateType.as_view(), name='create_type'),
    path('list_type', ListViewType.as_view(), name='list_type'),
    path('update/<pk>/', UpdateType.as_view(), name='update_type'),
    path('delete/<pk>/', DeleteType.as_view(), name='delete_type'),
]