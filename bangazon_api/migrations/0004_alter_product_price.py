# Generated by Django 3.2.9 on 2021-11-29 21:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazon_api', '0003_auto_20211129_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(17500.0)]),
        ),
    ]
