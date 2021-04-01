# Generated by Django 3.1.7 on 2021-04-01 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_auto_20210401_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 1, 12, 43, 26, 623066, tzinfo=utc)),
        ),
    ]
