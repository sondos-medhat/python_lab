# Generated by Django 3.1.7 on 2021-03-20 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210320_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='img',
        ),
    ]
