# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy


class Entry(models.Model):
    name = models.CharField(verbose_name=u'Заголовок', max_length=255)
    date_create = models.DateTimeField(verbose_name=u'Дата создания',
                                       auto_now_add=True)
    description = models.TextField(verbose_name=u'Описание')
    text = models.TextField(verbose_name=u'Текст')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        app_label = 'blog'
        ordering = ['-date_create']
        verbose_name = u'Запись блога'
        verbose_name_plural = u'Записи блога'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('blog:entry', kwargs={'pk': self.id})


class UserFeed(models.Model):
    # Подписка пользователя
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=u'Кто подписан',
                             related_name='user_feed')
    feed = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=u'На кого подписан',
                             related_name='user_readers')

    class Meta:
        app_label = 'blog'
        unique_together = (('user', 'feed'),)


class ReadEntry(models.Model):
    # Прочтенные посты
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='autor')
    entry = models.ForeignKey(Entry)

    class Meta:
        app_label = 'blog'
        unique_together = (('user', 'entry'),)
