from django.contrib import admin

from .models import PreworkVideo


@admin.register(PreworkVideo)
class PreworkVideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    fields = ('title', 'video_link', 'created', 'subject', 'unit', ('class_date', 'video_num'), 'slug', 'notes')
    list_display = ('title', 'created', 'subject', 'unit', 'full_video_id')
    list_filter = ['created', 'subject', 'unit']
    search_fields = ['title']

