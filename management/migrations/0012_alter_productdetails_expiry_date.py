# Generated by Django 4.1 on 2022-10-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_alter_productdetails_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
