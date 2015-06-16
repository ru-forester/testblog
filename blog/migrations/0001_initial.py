# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
            ],
            options={
                'ordering': ['-date_create'],
                'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c \u0431\u043b\u043e\u0433\u0430',
                'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438 \u0431\u043b\u043e\u0433\u0430',
            },
        ),
        migrations.CreateModel(
            name='ReadEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry', models.ForeignKey(to='blog.Entry')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feed', models.ForeignKey(related_name='user_readers', verbose_name='\u041d\u0430 \u043a\u043e\u0433\u043e \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u043d', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='user_feed', verbose_name='\u041a\u0442\u043e \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u043d', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
