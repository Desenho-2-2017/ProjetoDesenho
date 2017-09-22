# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 17:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170922_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(help_text='Preço atual do produto', validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Preço do produto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(help_text='Quantidade do produto em estoque', verbose_name='Quandtidade do produto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=0, help_text='Peso do produto atual', validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Peso do produto'),
        ),
    ]
