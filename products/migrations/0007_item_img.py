# Generated by Django 3.1.7 on 2021-03-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_item_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]