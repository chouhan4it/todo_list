# Generated by Django 4.1.3 on 2022-11-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todoitem_is_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={},
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='is_status',
            field=models.BooleanField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', verbose_name='Status?'),
        ),
    ]
