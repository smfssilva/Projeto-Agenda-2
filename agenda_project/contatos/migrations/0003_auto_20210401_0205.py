# Generated by Django 3.1.7 on 2021-04-01 02:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20210331_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 2, 5, 30, 646608, tzinfo=utc)),
        ),
    ]
