# Generated by Django 4.1.2 on 2024-06-24 01:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_rename_apellidos_usuario_apellido_usuario_contrasena_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='fecha_cuanta',
            new_name='fechaCreacion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombreUsuario',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
