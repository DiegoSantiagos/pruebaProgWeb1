# Generated by Django 4.1.2 on 2024-06-24 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_remove_carrito_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
