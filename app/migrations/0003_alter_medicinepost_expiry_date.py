# Generated by Django 3.2.5 on 2021-09-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210901_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='expiry_date',
            field=models.DateField(blank=True, default='2022-05-14', null=True, verbose_name='Expiry Date'),
        ),
    ]
