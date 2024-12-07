from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Task

from .forms import TaskForm

def index(request):
    return HttpResponse("HelloWorld!")


def taskList(request):

    form =TaskForm()

    tasks = Task.objects.all()


    if request.method =='POST':
        form= TaskForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                print("Form saved")
            except: 
                print("Hata")
            
            return redirect('/tasklist')

        

    context = {'tasks':tasks,'TaskForm':form}

    return render(request,'base/tasklist.html',context)
    
