# Generated by Django 3.2.3 on 2021-07-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csthirdparty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256)),
                ('add_date', models.DateField()),
            ],
        ),
    ]
