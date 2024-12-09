from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

from .forms import TaskForm


def index(request):
    return HttpResponse("HelloWorld!")


def taskList(request):

    if request.method == 'GET':

        form = TaskForm()

        tasks = Task.objects.all()

        context = {'tasks': tasks, 'TaskForm': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                print("Form saved")
            except:
                print("Hata")

            return redirect('/tasklist')

    return render(request, 'base/tasklist.html', context)


def updateTask(request, pk):

    if request.method == 'GET':

        task = Task.objects.get(id=pk)

        form = TaskForm(instance=task)

        print("Update form loaded.")
        context = {'TaskForm': form}

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()
            print("Update executed.")
            return redirect('/tasklist')

    return render(request, 'base/updatetask.html', context)


def deleteTask(request, pk):
    if request.method == 'GET':
        print("Delete form opened.")
        task = Task.objects.get(id=pk)
        context = {'task': task}
        return render(request, 'base/deletetask.html', context)

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        print("POST PK:"+pk)
        print("Delete executed.")
        task.delete()
        return redirect('tasklist')
