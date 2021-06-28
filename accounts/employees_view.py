from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import User
from django.contrib.messages import error, success
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required()
def update_password(request, pk):
    if request.method == "POST":
        form_data = request.POST
        if form_data['password1'] == form_data['password2'] and len(form_data['password1']) > 7:
            u = User.objects.get(pk=pk)
            u.set_password(form_data['password1'])
            success(request, "Password Update Successfully ")
            u.save()
            return redirect(reverse('accounts:listView'))
        else:
            error(request, "The Passwords Do Not Match or needs to be more that 8 characters")
            return render(request, "accounts/employees/change_password.html", context={'pk': pk})

    return render(request, "accounts/employees/change_password.html", context={'pk': pk})


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/employees/profile.html'


class AccountsListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 15
    template_name = "accounts/employees/listView.html"


class AccountsUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ('username',
              'first_name',
              'last_name',
              'email',
              'image',
              'location',
              'is_admin',
              'is_supervisor',
              )
    template_name = 'accounts/employees/user_update_form.html'
    success_url = reverse_lazy('accounts:listView')


class AccountsDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('accounts:listView')
    template_name = 'accounts/employees/user_confirm_delete.html'