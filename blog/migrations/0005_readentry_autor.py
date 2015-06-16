# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20150616_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='readentry',
            name='autor',
            field=models.ForeignKey(related_name='autor', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
