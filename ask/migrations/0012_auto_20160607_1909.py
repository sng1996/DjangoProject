# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0011_auto_20160607_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(to='ask.Question'),
        ),
    ]
