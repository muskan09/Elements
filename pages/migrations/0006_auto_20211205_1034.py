# Generated by Django 3.2.9 on 2021-12-05 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20211205_0928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Domains',
            new_name='Domain',
        ),
        migrations.RenameModel(
            old_name='Languages',
            new_name='Language',
        ),
        migrations.RenameModel(
            old_name='Platforms',
            new_name='Platform',
        ),
    ]
