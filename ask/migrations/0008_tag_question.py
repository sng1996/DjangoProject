# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0007_profile_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ManyToManyField(related_name='tagOfQuestion', to='ask.Question'),
        ),
    ]
