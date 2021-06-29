import os
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tools.forms import TempImageForm
from django.db.models import Count
from tools.models import TempImage
from tools.data_processing.barcode_scanner import get_barcode_info
from django.contrib.messages import success,error
from tools.models import Tool


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
            image_data, image_path = get_barcode_info(obj)

            if image_data:
                try:
                    tool = Tool.objects.get(code=image_data)
                    return redirect(f"{reverse('tools:receive_tool')}{image_data}")
                except Tool.DoesNotExist:
                    return redirect(f"{reverse('tools:create_tool')}/{image_data}")
        return redirect(f"{reverse('tools:create_tool')}")

