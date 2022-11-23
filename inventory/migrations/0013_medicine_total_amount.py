# Generated by Django 4.0.4 on 2022-11-23 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0070_todaypatients_is_seperated'),
        ('inventory', '0012_alter_medicine_medicine_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine_total_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patientdetails')),
                ('vitals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.generalvitals_new')),
            ],
        ),
    ]
