# Generated by Django 5.0.3 on 2024-04-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='car_images/'),
        ),
    ]