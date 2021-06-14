from django.shortcuts import render
from django.views.generic import View


class PrivateArea(View):
    def get(self, request):
        return render(request, 'private_area/index.html')

