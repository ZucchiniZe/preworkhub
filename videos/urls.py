from django.urls import path

from . import views

app_name = 'videos'
urlpatterns = [
    path('', views.index, name='index'),
    path('video/<str:subject>/<slug:slug>', views.show_video, name='show_video')
]
