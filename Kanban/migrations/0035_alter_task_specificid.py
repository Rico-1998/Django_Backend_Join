# Generated by Django 4.1.7 on 2023-03-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0034_task_created_date_task_specificid_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='specificID',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
