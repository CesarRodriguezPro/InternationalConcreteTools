from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, employees_view

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/signup.html'), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),

    #  employees management
    path('listView/', employees_view.AccountsListView.as_view(), name='listView'),
    path('update/<pk>/', employees_view.AccountsUpdate.as_view(), name='updateView'),
    path('password_update/<pk>/', employees_view.update_password, name='password_update'),
    path('delete/<pk>/', employees_view.AccountsDelete.as_view(), name='deleteView'),

]