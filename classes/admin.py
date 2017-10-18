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


class ClassDateAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'day', 'date')
    list_filter = ('subject',)
    search_fields = ['video__title']
    inlines = (VideoInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(ClassDate, ClassDateAdmin)
