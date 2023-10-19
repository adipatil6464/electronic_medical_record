# Generated by Django 4.2.3 on 2023-10-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0020_alter_payment_doctor_id_alter_payment_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000)),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('order_id', models.CharField(max_length=1000)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=1000)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
