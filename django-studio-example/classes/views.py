import json
from functools import reduce
from pprint import pprint
import re
from django.forms import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DanceClassForm
from .models import DanceClass, Teacher

def index(request):
    classes = DanceClass.objects.all()
    form = DanceClassForm()
    context = {
        'classes': classes, 
        'form': form
        }

    return render(request, 'classes/home.html', context=context)

def add_class(request):
    if request.method == "POST":
        print(request.POST)
        form = DanceClassForm(request.POST)
        if form.is_valid():
            new_class = form.save()
            return redirect("home")
    else:
        form = DanceClassForm()
    return render(request, 'classes/add_class.html', {'form': form})

# convert above view to JSON response
def ajax_add_class(request):
    data = {}
    if request.method == "POST":
        pprint(request.POST)
        class_name = request.POST.get('name') 
        form = DanceClassForm(request.POST)

        if form.is_valid():
            new_class = form.save()
            data['saved'] = True
        else:
            data['saved'] = False
        data['class_name'] = class_name

    else:
        data['response': 'nothing to get']
    return JsonResponse(data)

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

def ajax_add_teacher(request):
    if request.method == 'POST':
        print(request.POST)
        teacher_name = request.POST.get('teacher-name')
        teacher = Teacher.objects.create(name=teacher_name)
        data = {
            'new_teacher': 'created',
            'name': teacher.name
        }
    else:
        data = {'status': 'not ok'}
    print(data)
    return JsonResponse(data)
