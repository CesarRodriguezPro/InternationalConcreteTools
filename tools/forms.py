from django import forms
from .models import Tool, Type, TempImage


class CreateTypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'


class TempImageForm(forms.Form):
    image = forms.ImageField()

