from django.shortcuts import render
from .models import Todo
from forms import TodoAddForm

def home(request):
    return render(request, 'todo/home.html')

def todolist(request):
    todos = Todo.object.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todo/todolist.html', context)

def todo_create(request):
    form = TodoAddForm()
    context = {
        'form':form,
    }
    return render(request,'todo/todo_create.html', context)