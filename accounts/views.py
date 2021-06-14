from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = 'You Succesfully Sign Up'


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
