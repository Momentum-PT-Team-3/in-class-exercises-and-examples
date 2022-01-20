from django.forms import ModelForm
from .models import DanceClass


class DanceClassForm(ModelForm):
    class Meta:
        model = DanceClass
        fields = ['name', 'time', 'length', 'teachers']


 