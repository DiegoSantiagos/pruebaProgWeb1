# Generated by Django 5.0.6 on 2024-07-17 00:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_carrito_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='registroCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.direccion')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.metodopago')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.productos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
