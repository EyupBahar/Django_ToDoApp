from django.urls import path
from .views import home, todolist, todo_create, todo_update

urlpatterns = [
    path('', home, name='home'),
    path('list/', todolist, name='todolist'),
    path('create/', todo_create, name='todo_create'),
    path('<int:id>/update', todo_update, name='todo_update'), #single bir objeyi id si ile alma
]
