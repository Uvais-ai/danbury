# Generated by Django 3.2.20 on 2023-08-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20230817_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimages',
            name='cat',
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='fitness',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='healthy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='galleryimages',
            name='works_out',
            field=models.BooleanField(default=False),
        ),
    ]
