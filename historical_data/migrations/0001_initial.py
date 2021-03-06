# Generated by Django 3.2.7 on 2021-09-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(default='None', max_length=10)),
                ('date', models.DateField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('adj_close', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
