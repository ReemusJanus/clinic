# Generated by Django 4.1.2 on 2022-10-25 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0055_alter_addfees_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addfees',
            name='patient',
        ),
    ]
