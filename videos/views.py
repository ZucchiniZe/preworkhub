from django.shortcuts import get_object_or_404, render

from .models import PreworkVideo


def index(request):
    stats = PreworkVideo.objects.filter(subject='stats')
    calc = PreworkVideo.objects.filter(subject='calc')
    return render(request, 'videos/index.html', {'stats': stats, 'calc': calc})


def list_videos(request, subject):
    videos = PreworkVideo.objects.filter(subject=subject)
    if len(videos) > 0:
        subj = videos[0].subject_verbose()
    else:
        subj = subject
    return render(request, 'videos/list_videos.html', {'videos': videos, 'subject': subj})


def show_video(request, subject, slug):
    video = get_object_or_404(PreworkVideo, slug=slug)
    return render(request, 'videos/show_video.html', {'video': video})
