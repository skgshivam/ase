# Generated by Django 2.1.2 on 2018-11-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0002_auto_20181101_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]