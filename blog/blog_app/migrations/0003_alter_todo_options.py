# Generated by Django 5.1.4 on 2024-12-11 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_todo_alter_category_options_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
