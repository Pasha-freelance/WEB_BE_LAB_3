# Generated by Django 4.2.13 on 2024-06-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_alter_person_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileId',
            field=models.CharField(default='78711e6b-0752-4499-985a-706b417806a9', max_length=255),
        ),
    ]
