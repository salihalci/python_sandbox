from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('tasklist/', views.taskList, name="tasklist"),
    path('updatetask/<str:pk>', views.updateTask, name="updatetask"),
    path('deletetask/<str:pk>', views.deleteTask, name="deletetask"),
    

]