# Generated by Django 5.0.7 on 2024-08-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_documento_pagado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolesusuario',
            name='rol',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('SECRETARIA', 'Secretaria'), ('USUARIO', 'Usuario'), ('TESORERIA', 'Tesorería')], default='USUARIO', max_length=10),
        ),
    ]