from django.contrib import admin

from models import Entry, UserFeed, ReadEntry


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ['name', 'user']

admin.site.register(Entry, EntryAdmin)
admin.site.register(UserFeed)
admin.site.register(ReadEntry)
