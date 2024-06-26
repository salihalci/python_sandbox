from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from .models import Todo

def home(request):
    return render(request,'todo/home.html')
# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        #Create a new user submit button clicked
        if request.POST['password1'] == request.POST['password2']:
          
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])

                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Username has already been taken!'})

        else:
            #Password did not match
            return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'Passwords did not match!'})


def currenttodos(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/currenttodos.html',{'todos':todos})


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'], password = request.POST['password'])
        login(request, user)
        return redirect('currenttodos')
        
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),'error':'Username and password did not match!'})
        else:
            login(request, user)
            return redirect('currenttodos')


def createtodo(request):
    if request.method == 'GET': #create todo formunun gösterildiği durum
        return render(request, 'todo/createtodo.html', {'form': TodoForm() })
    else: #submit butonuna basıldığı durum
        if request.method == 'POST':   
            try:    
                form = TodoForm(request.POST)
                newTodo = form.save(commit=False)
                newTodo.user = request.user
                newTodo.save()
                return redirect('currenttodos')
            except ValueError:
                return render(request, 'todo/createtodo.html', {'form': TodoForm(),'error':'Bad data passed in' })
