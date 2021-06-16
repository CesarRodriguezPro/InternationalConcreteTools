from django.forms import ModelForm
from .views import Tool, Type

class CreateToolForm(ModelForm):
    class Meta:
        model = Tool
        fields = ['type', 'tags', 'quantity']


class CreateTypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'
