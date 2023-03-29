# Generated by Django 4.1.7 on 2023-03-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0019_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='prio',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default=('H', 'High'), max_length=1),
        ),
    ]
