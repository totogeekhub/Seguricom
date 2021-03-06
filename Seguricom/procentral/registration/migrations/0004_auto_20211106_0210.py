# Generated by Django 3.2.9 on 2021-11-06 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_tipoempresa_nombre_emp'),
        ('registration', '0003_auto_20211106_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telefono',
            field=models.TextField(blank=True, null=True, verbose_name='Contacto'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rubro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.tipoempresa', verbose_name='Empresa'),
        ),
    ]
