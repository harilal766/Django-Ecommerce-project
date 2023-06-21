# Generated by Django 4.2.1 on 2023-06-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='Pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]
