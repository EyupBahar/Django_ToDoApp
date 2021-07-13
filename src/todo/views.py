from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def home_page(request):
    return render(request, 'todo/home.html') 