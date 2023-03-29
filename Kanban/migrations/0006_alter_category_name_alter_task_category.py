# Generated by Django 4.1.7 on 2023-03-12 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0005_category_colour_category_name_task_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='1', max_length=30),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Kanban.category'),
        ),
    ]
