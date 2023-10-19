# Generated by Django 4.2.3 on 2023-10-18 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0018_confirmappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meds.doctorid')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meds.patientid')),
            ],
        ),
    ]