import re
from django.db import models


class PreworkVideo(models.Model):
    CALCULUS = 'calc'
    STATISTICS = 'stat'
    CLASS_CHOICES = (
        (CALCULUS, 'Calculus'),
        (STATISTICS, 'Statistics'),
    )

    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=4, choices=CLASS_CHOICES)
    video_link = models.CharField(max_length=100)

    # These are SmallIntegerFields because we aren't going to be having class numbers above 32767
    class_num = models.SmallIntegerField()
    video_num = models.SmallIntegerField(default=1)

    slug = models.SlugField()

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def video_id(self):
        pattern = re.compile('(0[A-Z])\w+')
        match = pattern.search(self.video_link)
        if match:
            return match.group()
        else:
            return ''

    @property
    def embed_link(self):
        return f"https://drive.google.com/file/d/{self.video_id}/preview"
