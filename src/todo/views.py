from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoAppForm

def home(request):
    return render(request, 'todo/home.html')

def todolist(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todo/todolist.html', context)

def todo_create(request):
    form = TodoAddForm()
    if request.method == 'POST':
        form = TodoAddForm(request, POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    context = {
        'form':form,
    }
    return render(request,'todo/todo_create.html', context)

def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todolist")

        context = {
            'form':form
        } 
        return render(request, 'todo/todo_update.html', context)