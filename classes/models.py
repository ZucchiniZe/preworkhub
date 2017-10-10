from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Subject(models.Model):
    CALCULUS = 'calc'
    STATISTICS = 'stats'
    CLASS_CHOICES = (
        (CALCULUS, 'Calculus'),
        (STATISTICS, 'Statistics'),
    )

    name = models.CharField(db_index=True, max_length=5, choices=CLASS_CHOICES)
    grade = models.IntegerField(default=12)
    announcement = models.TextField(blank=True)

    def __str__(self):
        return self.subject_verbose()

    def subject_verbose(self):
        return dict(Subject.CLASS_CHOICES)[self.name]


class ClassDate(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.IntegerField(db_index=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.subject} day {self.day}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
