# Generated by Django 5.0.3 on 2024-04-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Confirmed', max_length=50),
        ),
    ]
