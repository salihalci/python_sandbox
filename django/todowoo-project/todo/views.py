from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        #Create a new user submit button clicked
        if request.POST['password1'] == request.POST['password2']:
          user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
          user.save()
          return render(request,'todo/signupuser.html',{'form':UserCreationForm()})
        else:
            #Password did not match
            print("password did not match")
            pass
