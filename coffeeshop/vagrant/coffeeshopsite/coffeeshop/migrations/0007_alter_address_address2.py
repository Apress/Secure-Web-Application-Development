# Generated by Django 3.2.7 on 2021-10-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0006_alter_address_address2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
