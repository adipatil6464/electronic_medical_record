# Generated by Django 4.2.3 on 2023-10-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0003_remove_patientdocument_patient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_experties',
            field=models.CharField(default='opd', max_length=100),
        ),
    ]