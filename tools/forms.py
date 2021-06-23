from django.forms import ModelForm
from .views import Tool, Type


class CreateTypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

