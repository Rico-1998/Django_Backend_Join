# Generated by Django 4.1.7 on 2023-03-19 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0041_alter_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='prio',
            new_name='urgency',
        ),
    ]
