# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150616_0635'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='readentry',
            unique_together=set([('user', 'entry')]),
        ),
    ]
