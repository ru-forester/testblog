# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from models import Entry, UserFeed, ReadEntry

User = get_user_model()


class EntryListView(ListView):
    model = Entry

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        if 'pk' in self.kwargs:
            user = get_object_or_404(User, pk=self.kwargs['pk'])
            context['page_name'] = u'Блог имени ' + str(user)
            # Проверяем подписан или нет
            if self.request.user.is_authenticated() and user != self.request.user:
                context['not_autor'] = True
                context['autor'] = user
                try:
                    context['is_reader'] = bool(UserFeed.objects.get(user=self.request.user, feed=user))
                except UserFeed.DoesNotExist:
                    context['is_reader'] = False
        else:
            context['page_name'] = u'Общий блог'
        return context

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Entry.objects.filter(user=self.kwargs['pk'])
        else:
            return Entry.objects.all()


@login_required
def add_feed(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        UserFeed.objects.create(user=request.user, feed=user)
    except IntegrityError:
        pass
    return HttpResponseRedirect(reverse('blog:user', kwargs={'pk': user_id}))


@login_required
def delete_feed(request, user_id):
    UserFeed.objects.filter(user=request.user, feed=user_id).delete()
    ReadEntry.objects.filter(user=request.user, autor=user_id).delete()
    return HttpResponseRedirect(reverse('blog:user', kwargs={'pk': user_id}))


@login_required
def add_to_read(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    try:
        ReadEntry.objects.create(user=request.user, autor=entry.user, entry=entry)
    except IntegrityError:
        pass
    return HttpResponseRedirect(reverse('blog:entry', kwargs={'pk': entry_id}))


class FeedListView(ListView):
    model = Entry
    template_name = 'blog/entry_list.html'

    def get_context_data(self, **kwargs):
        context = super(FeedListView, self).get_context_data(**kwargs)
        context['page_name'] = u'Мои подписки'
        context['feed_autors'] = self.request.user.user_feed.all()
        return context

    def get_queryset(self):
        autors = self.request.user.user_feed.values('feed')
        autors = [a['feed'] for a in autors]
        return Entry.objects.filter(user__in=autors)


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'blog/entry.html'

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            autors = self.request.user.user_feed.values('feed')
            autors = [a['feed'] for a in autors]
            context['in_feed'] = context['object'].user.id in autors
            if context['in_feed']:
                try:
                    is_r = ReadEntry.objects.get(user=self.request.user,
                                                 entry=self.kwargs['pk'])
                    context['is_ready'] = bool(is_r)
                except ReadEntry.DoesNotExist:
                    context['is_ready'] = False

        return context


class EntryCreate(CreateView):
    model = Entry
    fields = ['name', 'description', 'text']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())
