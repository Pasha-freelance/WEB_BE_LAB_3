# Generated by Django 4.2.13 on 2024-05-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_deadline_alter_todo_identifier_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='identifier',
            field=models.CharField(default='18627c6d-dc20-4780-bd24-7b89926f4f8b', max_length=255, unique=True, verbose_name='Identifier'),
        ),
    ]
