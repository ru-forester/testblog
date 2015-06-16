from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from views import (EntryCreate, EntryDetailView, FeedListView,
                   EntryListView, add_feed, delete_feed, add_to_read)


urlpatterns = [
    url(r'^add/$', login_required(EntryCreate.as_view()), name='entry_add'),
    url(r'entry/(?P<pk>[0-9]+)/$', EntryDetailView.as_view(), name='entry'),
    url(r'user/(?P<pk>[0-9]+)/$', EntryListView.as_view(), name='user'),
    url(r'add_feed/(?P<user_id>[0-9]+)/$', add_feed, name='add_feed'),
    url(r'delete_feed/(?P<user_id>[0-9]+)/$', delete_feed, name='delete_feed'),
    url(r'^feed/$', login_required(FeedListView.as_view()), name='user_feed'),
    url(r'^add_to_read/(?P<entry_id>[0-9]+)/$', add_to_read, name='add_to_read'),
]
