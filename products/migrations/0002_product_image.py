# Generated by Django 3.0.4 on 2020-03-26 10:57

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=products.models.path_and_rename),
        ),
    ]
