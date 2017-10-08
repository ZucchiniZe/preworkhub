from django.shortcuts import get_object_or_404, render

from .models import PreworkVideo


def index(request):
    return render(request, 'videos/index.html')


def list_videos(request, subject):
    videos = PreworkVideo.objects.filter(subject__exact=subject)
    return render(request, 'videos/list_videos.html', {'videos': videos, 'subject': subject})


def show_video(request, subject, slug):
    video = get_object_or_404(PreworkVideo, slug=slug)
    return render(request, 'videos/show_video.html', {'video': video})
