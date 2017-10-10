import re
from datetime import date
from django.db import models


class PreworkVideo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField('Date created', default=date.today)
    # subject = models.CharField(db_index=True, max_length=5, choices=CLASS_CHOICES)
    subject = models.ForeignKey('classes.Subject', db_index=False, on_delete=models.PROTECT)
    video_link = models.CharField(max_length=100)

    # These are SmallIntegerFields because we aren't going to be having class numbers above 32767
    # class_num = models.SmallIntegerField()
    class_date = models.ForeignKey('classes.ClassDate', on_delete=models.PROTECT)
    video_num = models.SmallIntegerField(default=1)

    slug = models.SlugField('URL', unique=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

    @property
    def video_id(self):
        pattern = re.compile('(0[A-Za-z0-1])\w+')
        match = pattern.search(self.video_link)
        if match:
            return match.group()
        else:
            return ''

    @property
    def embed_link(self):
        return f"https://drive.google.com/file/d/{self.video_id}/preview"

    @property
    def full_video_id(self):
        return f"{self.class_date.day}-{self.video_num}"
    full_video_id.fget.short_description = 'Class and Video Number'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('videos:show_video', args=[self.subject, self.slug])

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'
