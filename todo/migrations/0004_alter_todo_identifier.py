# Generated by Django 4.2.13 on 2024-05-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='identifier',
            field=models.CharField(default='333df10f-9ad3-43b6-b53c-e6f573f59d3e', max_length=255, unique=True, verbose_name='Identifier'),
        ),
    ]
