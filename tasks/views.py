from django.shortcuts import render, redirect
from .models import Task

def TaskAddHome(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Task.objects.create(name=name)
        return redirect('/')
    tasks = Task.objects.all().order_by('-pk')
    return render(request, 'index.html', {'tasks': tasks})

def taskcomplete(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        if task.completed == True:
            task.completed = False
            task.save()
        else:
            task.completed = True
            task.save()
        return redirect('/')

def taskdelete(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('/')
