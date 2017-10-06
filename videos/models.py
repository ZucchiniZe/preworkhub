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

    # These are SmallIntegerFields because we aren't going to be having class numbers above 32767
    class_num = models.SmallIntegerField()
    video_num = models.SmallIntegerField()

    slug = models.SlugField()  # TODO: Should be prepopulated with f"{class_num}v{video_num}" f"{class_num}.{video_num}"

    notes = models.TextField()
    video_link = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    @property
    def video_id(self):
        pattern = re.compile('d\/(0[A-Z])\w+\/view')
        match = pattern.match(self.video_link)
        if match:
            return match.lastgroup()
        else:
            return ''
