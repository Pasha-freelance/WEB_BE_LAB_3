# Generated by Django 4.2.13 on 2024-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_emaillog_alter_person_profileid_alter_todo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileId',
            field=models.CharField(default='3e3fd3c9-f820-4caa-aeb0-474440e2cc3e', max_length=255),
        ),
    ]
