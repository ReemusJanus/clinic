# Generated by Django 4.1 on 2022-10-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_productdetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='date',
            field=models.DateField(),
        ),
    ]
