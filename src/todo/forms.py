from django import forms
from .models import Todo

class TodoAppForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'

class TodoUpdateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("title", "Completed")