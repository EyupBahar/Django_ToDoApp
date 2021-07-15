from django.urls import path
from .views import home, todolist, todo_create

urlpatterns = [
    path('', home, name='home'),
    path('list/', todolist, name='todolist'),
    path('create/', todo_create, name='todo_create'),
]
