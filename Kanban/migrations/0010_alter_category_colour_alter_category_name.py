# Generated by Django 4.1.7 on 2023-03-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0009_task_assigned_to_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='colour',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
