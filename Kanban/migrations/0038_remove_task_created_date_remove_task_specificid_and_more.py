# Generated by Django 4.1.7 on 2023-03-19 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0037_alter_task_specificid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_Date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='specificID',
        ),
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
