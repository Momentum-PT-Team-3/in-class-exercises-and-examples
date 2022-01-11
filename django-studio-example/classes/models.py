from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Class(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=10, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    teacher = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "classes"

    def __str__(self):
        return self.name
