# Generated by Django 3.2.9 on 2021-12-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20211205_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domains',
            name='more',
        ),
        migrations.RemoveField(
            model_name='languages',
            name='more',
        ),
        migrations.RemoveField(
            model_name='platforms',
            name='more',
        ),
        migrations.AddField(
            model_name='domains',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='languages',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='platforms',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
