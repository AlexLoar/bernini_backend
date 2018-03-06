# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
                ('description', models.CharField(max_length=200, verbose_name=b'Descripci\xc3\xb3n')),
                ('price', models.FloatField(verbose_name=b'Precio (\xe2\x82\xac)')),
            ],
            options={
                'verbose_name': 'Art\xedculos',
                'verbose_name_plural': 'Art\xedculos',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.CharField(max_length=200, verbose_name=b'Cliente')),
                ('total', models.FloatField(default=0.0, null=True, blank=True)),
                ('pay', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(verbose_name=b'Cantidad')),
                ('total', models.FloatField(verbose_name=b'Total', blank=True)),
                ('article', models.ForeignKey(related_name='billing_lines', verbose_name=b'Art\xc3\xadculo', to='orders.Article')),
                ('order', models.ForeignKey(related_name='lines', verbose_name=b'Factura', to='orders.Order')),
            ],
            options={
                'verbose_name': 'L\xednea de pedido',
                'verbose_name_plural': 'L\xedneas de pedido',
            },
        ),
    ]
