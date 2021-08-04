# Generated by Django 3.2.5 on 2021-08-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_medicinepost_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='post_type',
            field=models.CharField(choices=[('Donate', 'Donate'), ('Receive', 'Receive')], default='JANUARY', max_length=20),
        ),
    ]
