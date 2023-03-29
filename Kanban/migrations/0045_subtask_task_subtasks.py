# Generated by Django 4.1.7 on 2023-03-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0044_alter_task_assigned_to_alter_task_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=300)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(blank=True, to='Kanban.subtask'),
        ),
    ]
