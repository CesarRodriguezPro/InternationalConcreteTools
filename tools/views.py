from django.shortcuts import render
from django.views.generic import View,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tool, Type
from .forms import CreateToolForm, CreateTypeForm
from django.contrib.messages import success, error, views
from django.shortcuts import redirect
from django.urls import reverse_lazy


#  Tools Views
class Home(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'list_objects': Tool.objects.all(),
        }
        return render(request, 'tools/home.html', context)


class CreateTool(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'form': CreateToolForm(),
        }
        return render(request, 'tools/create_or_update_tool/create_tool.html', context)

    def post(self,request):
        context = {
            'form': CreateToolForm(),
        }
        form_data = request.POST
        print(form_data)
        return render(request, 'tools/create_or_update_tool/create_tool.html')


class CreateType(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'form': CreateTypeForm(),
        }
        return render(request, 'tools/type_templates/type_form.html',context)

    def post(self,request):
        form = CreateTypeForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, 'New Type Was created')
            return redirect('tools:create_type')
        error(request, 'There was a error ')
        return redirect('tools:create_type')


#  Types Views
class ListViewType(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'list_objects': Type.objects.all(),
        }
        return render(request,'tools/type_templates/listView.html', context )


class DeleteType(LoginRequiredMixin, DeleteView):
    model = Type
    template_name = 'tools/type_templates/type_confirm_delete.html'
    success_url = reverse_lazy('tools:list_type')


class UpdateType(LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
    model = Type
    fields = "__all__"
    template_name_suffix = 'tools/type_templates/type_form.html'
    success_url = reverse_lazy('tools:list_type')