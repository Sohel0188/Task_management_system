from django.shortcuts import render,redirect
from . import form
from .models import Task

# Create your views here.
def add(request):
    if request.method == "POST":
        formvalue =  form.TaskForm(request.POST)
        if formvalue.is_valid():
            
            formvalue.save()
            return redirect('home')
    else:
        formvalue = form.TaskForm()
    return render(request,'add_task.html',{'form': formvalue })

def edit(request,id):
    data = Task.objects.get(pk = id)
    form_data = form.TaskForm(instance=data)
    if request.method == "POST":
        form_data = form.TaskForm(request.POST, instance=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    return render(request,'edit_task.html',{'form': form_data })


def delete(request,id):
    data = Task.objects.get(pk = id)
    data.delete()
    return redirect('home')