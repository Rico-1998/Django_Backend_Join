# Generated by Django 4.1.7 on 2023-03-12 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0003_delete_subtasks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='prio',
        ),
    ]