from functools import reduce
from django.forms import forms
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DanceClassForm
from .models import DanceClass

def index(request):
    classes = DanceClass.objects.all()
    return render(request, 'classes/home.html', {'classes': classes})

def add_class(request):
    if request.method == "POST":
        form = DanceClassForm(request.POST)
        if form.is_valid():
            new_class = form.save()
            return redirect("home")
    else:
        form = DanceClassForm()
    return render(request, 'classes/add_class.html', {'form': form})

def edit_class(request, pk):
    selected_class = get_object_or_404(DanceClass, pk=pk)
    if request.method == "POST":
        form = DanceClassForm(request.POST)
        if form.is_valid():
            selected_class = form.save()
            return redirect("home")
    else:
        form = DanceClassForm(instance=selected_class)
    return render(request, 'classes/edit_class.html', {'form': form, 'selected_class': selected_class})