from django.utils import timezone
from django.contrib import admin
from django.db import models
from django.urls import reverse
# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    IS_STATUS_CHOICES = [
        (False, 'Pending'), 
        (True, 'Completed')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    
    is_status = models.BooleanField("Status", default=False,choices=IS_STATUS_CHOICES)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        #list_display = (self.title,self.due_date,self.is_status)
        return f"{self.title}: due {self.due_date}"

class Meta:
    ordering = ["due_date"]
