# Generated by Django 4.2 on 2023-05-29 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choose',
            name='images',
        ),
    ]