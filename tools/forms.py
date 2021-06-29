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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control form-control-lg'})

    image = forms.ImageField()




