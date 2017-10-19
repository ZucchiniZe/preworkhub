import re
from datetime import date
from django.db import models


class Video(models.Model):
    """
    The Video class is where the majority of the work is happening, storing the title, a link to the google drive file,
    storing a connection between the class date, subject and unit.
    """
    title = models.CharField(max_length=100)
    created = models.DateField('Date created', default=date.today)
    subject = models.ForeignKey('classes.Subject', on_delete=models.PROTECT, related_name='videos')
    unit = models.ForeignKey('classes.Unit', on_delete=models.PROTECT, related_name='videos')
    video_link = models.CharField(max_length=100)

    class_date = models.ForeignKey('classes.ClassDate', on_delete=models.PROTECT, related_name='videos')
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
        return reverse('prework:show_video', args=[self.subject, self.slug])

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'


class VideoMetadata(models.Model):
    """
    Should be created every time a user (read student) watches a video and confirms that they have indeed, "got it"
    """
    student = models.ForeignKey('classes.Student', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    got_it = models.BooleanField(default=False)
    watched = models.BooleanField(default=False)
