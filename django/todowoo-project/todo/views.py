from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'todo/currenttodos.html',{'todos':todos})

def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')
    return render(request, 'todo/completedtodos.html',{'todos':todos})

@login_required
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

@login_required
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

@login_required
def viewtodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    if request.method=='GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo,'form':form})
    else:
        try:
            form = TodoForm(request.POST,instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo,'form':form,'error':'There is an error!'})
@login_required    
def completetodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    if request.method=='POST':
        todo.dateCompleted = timezone.now()
        todo.save()
        print("Here")
        return redirect('currenttodos')
@login_required
def deletetodo(request,todo_pk,questions):
    todo = get_object_or_404(Todo,pk=todo_pk,user=request.user)
    
    if request.method=='POST':
        todo.delete()
        return redirect('currenttodos')
    