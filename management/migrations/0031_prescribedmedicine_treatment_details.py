# Generated by Django 4.1 on 2022-10-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0030_prescribedmedicine_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescribedmedicine',
            name='treatment_details',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
