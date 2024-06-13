from django.shortcuts import render
from Task.models import Task

def home(request):
    data = Task.objects.all()
    return render(request,'base.html',{ "value" : data})