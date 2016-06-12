# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0009_auto_20160426_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(to='ask.Question'),
        ),
    ]
