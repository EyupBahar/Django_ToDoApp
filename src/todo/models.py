from django.db import models

class Todo(models.Model):
    todo_number = models.IntegerField()
    todo_content = models.CharField(max_length=300)


    def __str__(self):
        return f"{self.todo_number} {self.todo_content}"
