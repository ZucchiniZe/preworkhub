from django.shortcuts import get_object_or_404, render

from .models import Video


def index(request):
    stats = Video.objects.select_related('subject', 'class_date').filter(subject__name='stats')[:10]
    calc = Video.objects.select_related('subject', 'class_date').filter(subject__name='calc')[:10]
    return render(request, 'videos/index.html', {'stats': stats, 'calc': calc})


def list_videos(request, subject):
    videos = Video.objects.select_related('subject', 'class_date').filter(subject__name=subject)
    return render(request, 'videos/list_videos.html', {'videos': videos, 'subject': subject})


def show_video(request, _subject, slug):
    """Subject is ignored because it isn't needed but it is part of the URL"""
    video = get_object_or_404(Video.objects.select_related('subject', 'class_date'), slug=slug)
    return render(request, 'videos/show_video.html', {'video': video})
