

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=40)),
                ('bank_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='bank_customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('card_no', models.CharField(max_length=20)),
                ('card_type', models.CharField(choices=[('Visa', 'Visa'), ('Rupay', 'Rupay'), ('Master Card', 'Master Card')], max_length=20)),
                ('card_cvv', models.IntegerField()),
                ('bank_balance', models.FloatField(default=3000)),
                ('Bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.bank')),
            ],
        ),
        migrations.CreateModel(
            name='OnlinePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=20)),
                ('amount_paid', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.bank_customer')),
            ],
        ),
    ]
