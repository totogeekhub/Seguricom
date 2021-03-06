# Generated by Django 3.2.9 on 2021-12-01 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.IntegerField(max_length=15, verbose_name='Run Prevencionista')),
                ('cargo', models.CharField(max_length=100, verbose_name='Descripcion del Cargo')),
                ('fecha_ingreso', models.DateField(blank=True, verbose_name='Fecha de Ingreso')),
                ('fecha_termino', models.DateField(blank=True, verbose_name='Fecha de Termino')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'ordering': ['user__username'],
            },
        ),
    ]
