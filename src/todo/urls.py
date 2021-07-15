from django.urls import path
from .views import home, todolist, todo_create, todo_update, todo_delete

urlpatterns = [
    path("", home, name="home"),
    path("list/", todolist, name="todolist"),
    path("create/", todo_create, name="todo_create"),
    path("<int:id>/update/", todo_update, name="todo_update"),
    path("<str:id>/delete/", todo_delete, name="todo_delete"),
]