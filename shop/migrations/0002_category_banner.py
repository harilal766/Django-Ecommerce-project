# Generated by Django 5.0 on 2023-12-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.FileField(blank=True, null=True, upload_to='shop/category'),
        ),
    ]