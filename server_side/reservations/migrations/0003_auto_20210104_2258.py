# Generated by Django 3.1.4 on 2021-01-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20210104_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(),
        ),
    ]