from django.contrib import admin
from .models import Todo

class TodoList(admin.ModelAdmin):
    list_display = ('task_number', 'task_name', 'task_des', 'due_date')
    list_filter = ('task_number', 'task_name', 'task_des', 'due_date')
    search_fields = ('task_number', 'task_name')
    ordering = ['task_number']


admin.site.register(Todo, TodoList)
