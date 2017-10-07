from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import PreworkVideo


def index(request):
    return HttpResponse('this is a response')


def show_video(request, subject, slug):
    video = get_object_or_404(PreworkVideo, slug=slug)
    return HttpResponse(f"showing {subject} video: '{video.title}'")