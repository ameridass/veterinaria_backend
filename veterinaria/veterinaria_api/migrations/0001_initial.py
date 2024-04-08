# Generated by Django 4.1 on 2024-04-08 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('rol', models.CharField(max_length=255)),
                ('especializacion', models.CharField(max_length=255)),
                ('contacto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('tipo', models.CharField(max_length=255)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('especie', models.CharField(max_length=255)),
                ('raza', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('historial_medico', models.TextField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.estado')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('motivo', models.CharField(max_length=255)),
                ('diagnostico', models.TextField()),
                ('tratamiento', models.TextField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.empleado')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.estado')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.paciente')),
                ('sala', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veterinaria_api.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('observaciones', models.TextField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.empleado')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.estado')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria_api.paciente')),
            ],
        ),
    ]