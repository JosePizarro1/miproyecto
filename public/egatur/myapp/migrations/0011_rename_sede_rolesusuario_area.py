# Generated by Django 5.0.7 on 2024-08-08 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_documento_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rolesusuario',
            old_name='sede',
            new_name='area',
        ),
    ]
