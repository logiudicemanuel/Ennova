# Generated by Django 4.1.4 on 2023-01-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_todo_options_remove_todo_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='imei',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='is_complete',
            new_name='seriale',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='ticket',
        ),
        migrations.AddField(
            model_name='todo',
            name='note',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='todo',
            name='stato',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='todo',
            name='tipo_guasto',
            field=models.TextField(default='', max_length=200),
        ),
    ]
