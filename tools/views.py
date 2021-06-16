from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tool, Type
from .forms import CreateToolForm, CreateTypeForm
from django.contrib.messages import success, error
from django.shortcuts import redirect



class Home(LoginRequiredMixin, View):

    context={
        'list_objects': Tool.objects.all(),
    }

    def get(self, request):
        return render(request, 'tools/home.html', self.context)


class CreateTool(LoginRequiredMixin, View):

    context = {
        'form': CreateToolForm(),
    }

    def get(self, request):
        return render(request, 'tools/create_or_update_tool/create_tool.html', self.context)

    def post(self,request):
        form_data = request.POST
        print(form_data)
        return render(request, 'tools/create_or_update_tool/create_tool.html')


class CreateType(LoginRequiredMixin, View):

    context = {
        'form': CreateTypeForm(),
    }

    def get(self, request):
        return render(request, 'tools/create_or_update_type/type_form.html', self.context)

    def post(self,request):
        form = CreateTypeForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, 'New Type Was created')
            return redirect('tools:create_type')
        error(request, 'There was a error ')
        return redirect('tools:create_type')