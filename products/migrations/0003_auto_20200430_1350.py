# Generated by Django 3.0.5 on 2020-04-30 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200430_1230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Task',
        ),
    ]