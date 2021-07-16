from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=300)
    created_date= models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
            ordering = ['-created_date'] # Last created on top

    def __str__(self):
        return self.title
