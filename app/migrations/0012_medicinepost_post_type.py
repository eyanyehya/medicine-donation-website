# Generated by Django 3.2.5 on 2021-08-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_medicinepost_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinepost',
            name='post_type',
            field=models.CharField(choices=[('donate', 'donate'), ('receive', 'receive')], default='JANUARY', max_length=9),
        ),
    ]
