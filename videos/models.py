from django.db import models


class PreworkVideo(models.Model):
    CALCULUS = 'calc'
    STATISTICS = 'stat'
    CLASS_CHOICES = (
        (CALCULUS, 'Calculus'),
        (STATISTICS, 'Statistics'),
    )
    subject = models.CharField(max_length=4, choices=CLASS_CHOICES, required=True)
    title = models.CharField()
