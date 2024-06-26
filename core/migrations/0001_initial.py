# Generated by Django 5.0.1 on 2024-05-03 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('apellido_cliente', models.CharField(max_length=50)),
                ('correo_cliente', models.CharField(max_length=50)),
                ('password_cliente', models.CharField(max_length=50)),
                ('cant_mantenciones_cli', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mecanico', models.CharField(max_length=50)),
                ('apellido_mecanico', models.CharField(max_length=50)),
                ('correo_mecanico', models.CharField(max_length=50)),
                ('password_mecanico', models.CharField(max_length=50)),
                ('cant_mantenciones_mec', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TipoConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('email_contacto', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=9)),
                ('info_adicional', models.CharField(max_length=200)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoconsulta')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_trabajo', models.CharField(max_length=50)),
                ('diagnostico', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('materiales', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='imagenes/')),
                ('estado_publicacion', models.CharField(choices=[('P', 'Pendiente'), ('R', 'Rechazado'), ('A', 'Aceptado')], default='P', max_length=1)),
                ('comentario_admin', models.CharField(blank=True, max_length=100)),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanico')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tiposervicio')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('desc_rechazo', models.CharField(max_length=150)),
                ('trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabajo')),
            ],
        ),
    ]
