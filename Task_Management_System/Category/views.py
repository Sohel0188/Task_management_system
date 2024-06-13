from django.shortcuts import render,redirect
from . import form
from . import models

# Create your views here.
def add(request):
    if request.method == 'POST':
        data = form.CategoryForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('home')
    else:
        data = form.CategoryForm()
    return render (request,'add_category.html',{'form':data})