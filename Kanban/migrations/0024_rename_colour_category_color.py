# Generated by Django 4.1.7 on 2023-03-14 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kanban', '0023_contact_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='colour',
            new_name='color',
        ),
    ]
