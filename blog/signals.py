# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template import Context, Template
from models import Entry, UserFeed


tpl = Template('''
Пользователь {{autor}} создал новый пост:

{{entry.description}}

Подробности тут http://{{server}}{{entry.get_absolute_url}}

''')


@receiver(post_save, sender=Entry)
def mail_sender(sender, **kwargs):
    if not kwargs['created']:
        return
    entry = kwargs['instance']
    autor = entry.user
    server = settings.ALLOWED_HOSTS[0]
    c = Context(locals())
    message = tpl.render(c)
    for reader in UserFeed.objects.filter(feed=autor):
        reader = reader.user
        # if not reader.email:
        #     continue
        send_mail('Новый пост на сайте', message, settings.EMAIL_HOST_USER,
                  [reader.email])
