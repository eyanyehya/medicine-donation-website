# Generated by Django 3.2.5 on 2021-11-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211108_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='test',
            field=models.CharField(default='', max_length=200),
        ),
    ]