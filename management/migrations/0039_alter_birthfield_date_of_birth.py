# Generated by Django 4.1.2 on 2022-10-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0038_birthfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthfield',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
