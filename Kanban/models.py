from django.db import models
from datetime import date
from django.conf import settings


# class Category(models.Model):


class category(models.Model):
    name = models.CharField(max_length=30, default='')
    color = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=20, default='')
    phone = models.IntegerField(default='')
    initial = models.CharField(max_length=3, default='')
    color = models.CharField(max_length=500, default='')

    def __str__(self) -> str:
        return f'{self.name} {self.id}'


class subtask(models.Model):
    description = models.CharField(max_length=300, default='')
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f'({self.id})'


class Task(models.Model):
    prios = [
        ('urgent', 'urgent'),
        ('medium', 'medium'),
        ('low', 'low'),
    ]
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    category = models.ForeignKey(
        category, on_delete=models.CASCADE, null=True)
    assigned_to = models.ManyToManyField(
        Contact, blank=True)
    due_date = models.DateField(default=date.today)
    status = models.CharField(max_length=30, default='toDo')
    created_Date = models.CharField(max_length=200, default='')
    specificId = models.CharField(max_length=200, default='')
    urgency = models.CharField(
        max_length=7,
        choices=prios,
        default=prios[0]
    )
    subtasks = models.ManyToManyField(subtask, blank=True)

    def __str__(self):
        return f'({self.id}) {self.title}'  # prefix #suffix
