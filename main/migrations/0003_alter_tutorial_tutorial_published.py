# Generated by Django 4.1.3 on 2022-11-27 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 27, 11, 59, 29, 823537), verbose_name='date published'),
        ),
    ]
