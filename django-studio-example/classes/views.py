from django.shortcuts import render
from .models import Class

def index(request):
    classes = Class.objects.all()
    return render(request, 'classes/home.html', {'classes': classes})