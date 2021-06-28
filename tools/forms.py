from django import forms
from .models import Tool, Type, TempImage


class CreateTypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

class CreateToolCodeForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['type', 'tags', 'quantity', 'active']

class CreateToolNoCodeForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['code', 'type', 'tags', 'quantity', 'active']

class TempImageForm(forms.Form):
    image = forms.ImageField()

