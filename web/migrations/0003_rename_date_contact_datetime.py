# Generated by Django 3.2.20 on 2023-08-12 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20230812_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='datetime',
        ),
    ]
