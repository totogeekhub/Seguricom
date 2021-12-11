# Generated by Django 3.2.9 on 2021-12-01 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0004_contrato_empresa_rubro_tiporubro_trabajador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prevencionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.IntegerField(max_length=15, verbose_name='Run Prevencionista')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prevencionista',
                'verbose_name_plural': 'Prevencionista',
                'ordering': ['user__username'],
            },
        ),
    ]
