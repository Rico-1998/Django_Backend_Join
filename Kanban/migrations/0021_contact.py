# Generated by Django 4.1.7 on 2023-03-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0020_task_prio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=20)),
                ('phone', models.IntegerField(default='')),
            ],
        ),
    ]
