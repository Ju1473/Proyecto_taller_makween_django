# Generated by Django 5.0.1 on 2024-05-22 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_reserva_estado_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='mecanico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.mecanico'),
        ),
    ]
