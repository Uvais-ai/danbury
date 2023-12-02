# Generated by Django 3.2.20 on 2023-08-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_galleryimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimages',
            name='select_1',
        ),
        migrations.RemoveField(
            model_name='galleryimages',
            name='select_2',
        ),
        migrations.RemoveField(
            model_name='galleryimages',
            name='select_3',
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
