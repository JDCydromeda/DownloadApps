# Generated by Django 3.2.4 on 2021-06-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Download', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='Description',
            field=models.TextField(max_length=500),
        ),
    ]
