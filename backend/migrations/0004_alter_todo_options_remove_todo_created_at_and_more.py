# Generated by Django 4.1.4 on 2023-01-07 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_todo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
    ]
