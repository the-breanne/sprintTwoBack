from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    task_number = models.CharField(max_length=50)
    task_name = models.TextField(max_length=360)
    task_des = models.TextField(max_length=360)
    due_date = models.TextField(max_length=360)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()
