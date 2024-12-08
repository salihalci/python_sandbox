from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

from .forms import TaskForm


def index(request):
    return HttpResponse("HelloWorld!")


def taskList(request):

    form = TaskForm()

    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                print("Form saved")
            except:
                print("Hata")

            return redirect('/tasklist')

    context = {'tasks': tasks, 'TaskForm': form}

    return render(request, 'base/tasklist.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    print("Update form loaded.")

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()
            print("Update executed.")
            return redirect('/tasklist')

    context = {'TaskForm': form}
    return render(request, 'base/updatetask.html', context)


def deleteTask(request, pk):
    print("Delete form opened.")
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        print("Delete executed.")
        task.delete()
        return redirect('tasklist')

    context = {'task': task}
    return render(request, 'base/deletetask.html', context)
