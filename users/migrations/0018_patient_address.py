# Generated by Django 3.0.10 on 2020-10-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_appointment_date_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
