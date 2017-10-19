from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Student, Subject, Unit, ClassDate
from prework.models import Video


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)


class VideoInline(admin.StackedInline):
    model = Video
    ordering = ('video_num',)
    extra = 1
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'video_link', 'created', 'subject', 'unit', ('class_date', 'video_num'), 'slug', 'notes')


class ClassDateAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date')
    list_filter = ('subject',)
    search_fields = ['videos__title']
    inlines = (VideoInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(ClassDate, ClassDateAdmin)
