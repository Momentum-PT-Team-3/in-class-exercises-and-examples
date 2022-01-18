from functools import reduce
from django.forms import forms
from django.shortcuts import render, redirect
from .forms import ClassForm
from .models import Class

def index(request):
    classes = Class.objects.all()
    return render(request, 'classes/home.html', {'classes': classes})

def add_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save()
            return redirect("home")
    else:
        form = ClassForm()
    return render(request, 'classes/add_class.html', {'form': form})
