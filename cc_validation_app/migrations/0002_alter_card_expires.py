# Generated by Django 5.1.2 on 2024-10-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc_validation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expires',
            field=models.DateField(verbose_name='expiry date'),
        ),
    ]
