# Generated by Django 3.2.9 on 2021-12-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='run',
            field=models.CharField(max_length=15, verbose_name='Run Prevencionista'),
        ),
    ]
