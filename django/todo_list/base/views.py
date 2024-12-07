from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    return HttpResponse("HelloWorld!")


def taskList(request):
     return render(request,'base/tasklist.html')
     #return HttpResponse("tasklist!")
