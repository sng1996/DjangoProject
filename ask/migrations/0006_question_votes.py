# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask', '0005_auto_20160426_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(related_name='voted_users', through='ask.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
