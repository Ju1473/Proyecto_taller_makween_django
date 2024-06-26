# Generated by Django 5.0.4 on 2024-05-21 21:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_trabajo_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email_contacto',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('email_reserva', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^\\d{9}$', 'El número de teléfono debe tener 9 dígitos numéricos.')])),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tiposervicio')),
            ],
        ),
    ]
