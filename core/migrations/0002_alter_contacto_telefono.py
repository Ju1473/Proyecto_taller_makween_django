# Generated by Django 5.0.4 on 2024-05-15 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999), django.core.validators.MinValueValidator(100000000)]),
        ),
    ]
