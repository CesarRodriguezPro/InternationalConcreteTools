from django.urls import path
from .import views

app_name = 'locations'

urlpatterns = [
    path('create/', views.LocationsCreateView.as_view(), name='create'),
    path('listView/', views.LocationListView.as_view(), name='listView'),
    path('update/<pk>/', views.LocationUpdate.as_view(), name='updateView'),
    path('delete/<pk>/', views.LocationDelete.as_view(), name='deleteView'),
]