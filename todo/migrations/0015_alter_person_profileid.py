# Generated by Django 4.2.13 on 2024-06-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_person_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileId',
            field=models.CharField(default='2ba54d93-657d-47c7-8a19-f010436408b7', max_length=255),
        ),
    ]