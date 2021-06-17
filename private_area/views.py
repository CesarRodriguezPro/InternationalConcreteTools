from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tools.views import Tool
from django.db.models import Count


class PrivateArea(LoginRequiredMixin, View):

    def get(self, request):

        if request.user.is_admin:
            data = Tool.objects.all().order_by('-date_updated')
            total_tools = Tool.objects.values("type").annotate(Count("id"))
        else:
            data = Tool.objects.filter(current_user=request.user).order_by('-date_updated')
            total_tools = Tool.objects.filter(current_user=request.user).values("type").annotate(Count("id"))

        context = {
            'object_list': data,
            'current_tools_type': total_tools
        }
        return render(request, 'private_area/index.html',context)
