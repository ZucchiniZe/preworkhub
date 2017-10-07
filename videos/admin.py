from django.contrib import admin

from .models import PreworkVideo


@admin.register(PreworkVideo)
class PreworkVideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('class_num', 'video_num')}
    fields = ('title', 'video_link', 'subject', ('class_num', 'video_num'), 'slug', 'notes')

