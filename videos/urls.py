from django.urls import path, register_converter

from classes import converters
from . import views

register_converter(converters.SubjectConverter, 'subj')

app_name = 'videos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<subj:subject>/', views.list_videos, name='list_videos'),
    path('video/<subj:subject>/<slug:slug>/', views.show_video, name='show_video'),
]
