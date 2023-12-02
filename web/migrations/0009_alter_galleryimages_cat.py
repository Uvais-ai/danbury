# Generated by Django 3.2.20 on 2023-08-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_galleryimages_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimages',
            name='cat',
            field=models.CharField(choices=[('Healthy Food', 'Healthy Food'), ('Workout', 'Workout'), ('Fitness', 'Fitness')], default=0, max_length=20),
        ),
    ]