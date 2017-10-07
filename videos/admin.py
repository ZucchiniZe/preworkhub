from django.contrib import admin

from .models import PreworkVideo


@admin.register(PreworkVideo)
class PreworkVideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'class_num', 'video_num')}
    fields = ('title', 'video_link', 'subject', ('class_num', 'video_num'), 'slug', 'notes')
    list_display = ('title', 'created', 'subject', 'full_video_id')
    list_filter = ['created', 'subject']
    search_fields = ['title']

