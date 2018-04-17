# Generated by Django 2.0.4 on 2018-04-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.CharField(max_length=3)),
                ('target_currency', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('exchange_rate', models.FloatField()),
            ],
        ),
    ]
