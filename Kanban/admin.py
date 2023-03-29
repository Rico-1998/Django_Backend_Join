from django.contrib import admin
from .models import Contact, category, Task, subtask

# Register your models here.
admin.site.register(category)
admin.site.register(Task)
admin.site.register(Contact)
admin.site.register(subtask)
