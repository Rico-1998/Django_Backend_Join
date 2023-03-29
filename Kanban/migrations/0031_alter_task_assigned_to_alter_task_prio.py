# Generated by Django 4.1.7 on 2023-03-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0030_alter_task_prio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, to='Kanban.contact'),
        ),
        migrations.AlterField(
            model_name='task',
            name='prio',
            field=models.CharField(choices=[('urgent', 'urgent'), ('medium', 'medium'), ('low', 'low')], default=('urgent', 'urgent'), max_length=7),
        ),
    ]
