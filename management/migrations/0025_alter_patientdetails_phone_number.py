# Generated by Django 4.1 on 2022-10-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_healthhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='Phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
