from django.db import models
from django.contrib.auth.models import AbstractUser

DAY_CHOICES = [
    ('MON', 'Monday'),
    ('TUES', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THURS', 'Thursday'),
]



class User(AbstractUser):
    pass


class DanceClass(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=5, choices=DAY_CHOICES, blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    teachers = models.ManyToManyField(to='Teacher', related_name="classes")
    style = models.ForeignKey(to='Style', on_delete=models.CASCADE, blank=True, null=True, related_name="classes")

    class Meta:
        verbose_name_plural = "classes"

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    cell_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

