from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home(request):
    return render(request, 'todo/home.html')

def todolist(request):
    todos = Todo.object.all()
    context = {
        
    }