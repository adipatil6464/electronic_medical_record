# Generated by Django 4.2.3 on 2023-10-10 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0004_doctor_doctor_experties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doctor_experties',
            new_name='doctor_specialization',
        ),
    ]
