from django.forms import ModelForm
from .models import Class


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'time', 'length', 'teacher']


 