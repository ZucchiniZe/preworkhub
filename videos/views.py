from django.shortcuts import get_object_or_404, render

from .models import PreworkVideo
from classes.models import Subject


def index(request):
    stats_subj = Subject.objects.get(name='stats')
    calc_subj = Subject.objects.get(name='calc')
    stats = PreworkVideo.objects.select_related('subject', 'class_date').filter(subject=stats_subj)[:10]
    calc = PreworkVideo.objects.select_related('subject', 'class_date').filter(subject=calc_subj)[:10]
    return render(request, 'videos/index.html', {'stats': stats, 'calc': calc})


def list_videos(request, subject):
    subj = Subject.objects.get(name=subject)
    videos = PreworkVideo.objects.select_related('subject', 'class_date').filter(subject=subj)
    return render(request, 'videos/list_videos.html', {'videos': videos, 'subject': subj})


def show_video(request, subject, slug):
    video = get_object_or_404(PreworkVideo, slug=slug)
    return render(request, 'videos/show_video.html', {'video': video})
