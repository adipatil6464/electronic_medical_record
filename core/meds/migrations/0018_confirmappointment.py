# Generated by Django 4.2.3 on 2023-10-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0017_alter_appointment_doctor_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100)),
                ('doctor_id', models.CharField(max_length=100)),
                ('contact_date', models.DateField(blank=True, null=True)),
                ('contact_time', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]