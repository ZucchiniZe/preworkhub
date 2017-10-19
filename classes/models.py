from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Subject(models.Model):
    """
    A subject for a course, such as statistics, calculus, or math iii.

    Needs to be added to the class choices for now.
    """
    CALCULUS = 'calc'
    STATISTICS = 'stats'
    CLASS_CHOICES = (
        (CALCULUS, 'Calculus'),
        (STATISTICS, 'Statistics'),
    )

    name = models.CharField(db_index=True, max_length=50, unique=True, choices=CLASS_CHOICES)
    grade = models.IntegerField(default=12)
    announcement = models.TextField(blank=True)

    def __str__(self):
        return self.subject_verbose()

    def subject_verbose(self):
        return dict(Subject.CLASS_CHOICES)[self.name]


class ClassDate(models.Model):
    """
    Each time the class has a time with the teacher constitutes a 'Class Date' (named as such because just 'class'
    conflicts with the reserved keyword in the python language).
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.IntegerField(db_index=True)
    date = models.DateField(default=date.today)
    after_class = models.TextField(blank=True)

    def __str__(self):
        return f'Day {self.day}, {self.subject} [{self.videos.first().title}]'

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'
        ordering = ['-date']
        get_latest_by = 'date'


class Unit(models.Model):
    """
    A unit in a specific subject.
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    number = models.IntegerField(default=1)
    start_date = models.DateField(default=date.today)
    performance_task_date = models.DateField(default=date.today)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    A way to associate the enrolled subjects with a particular user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
