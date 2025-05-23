# Generated by Django 5.0.2 on 2025-05-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_escolar_api', '0004_remove_maestros_edad_alter_alumnos_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('lugar', models.CharField(max_length=255)),
                ('estudiantes', models.BooleanField(default=False)),
                ('profesores', models.BooleanField(default=False)),
                ('publico_general', models.BooleanField(default=False)),
                ('programa_educativo', models.CharField(blank=True, max_length=255, null=True)),
                ('responsable', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('cupo_maximo', models.PositiveIntegerField()),
            ],
        ),
    ]
