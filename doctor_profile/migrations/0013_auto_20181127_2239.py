# Generated by Django 2.0.5 on 2018-11-27 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0012_auto_20181127_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.BookingDate'),
        ),
    ]
