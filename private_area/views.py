import os
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tools.views import Tool
from tools.forms import TempImageForm
from django.db.models import Count
from tools.models import TempImage
from tools.data_processing.barcode_scanner import get_barcode_info
from django.contrib.messages import ERROR
from pylibdmtx.pylibdmtx import decode


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
            'current_tools_type': total_tools,
            'temp_image_tool':TempImageForm()
        }
        return render(request, 'private_area/index.html',context)


    def post(self, request):
        form = TempImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            obj = TempImage(image = image)
            obj.save()
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ## working in this part

        return redirect("private_area:private_area")

