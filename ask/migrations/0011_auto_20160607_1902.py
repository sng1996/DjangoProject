# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0010_auto_20160605_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(related_name='question_tag', to='ask.Question'),
        ),
    ]
