# Generated by Django 4.2.13 on 2024-05-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_customuser_username_alter_todo_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='identifier',
            field=models.CharField(default='37f22adc-8184-4412-b779-e43fb9d3543c', max_length=255, unique=True, verbose_name='Identifier'),
        ),
    ]
