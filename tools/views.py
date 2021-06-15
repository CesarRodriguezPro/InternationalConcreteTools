from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tool, Type
from .forms import CreateToolForm



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