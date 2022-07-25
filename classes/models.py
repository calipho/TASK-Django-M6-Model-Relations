from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(
        Lecture, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(
        Lecture, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, related_name='tags')

    def __str__(self):
        return self.name

# Add a many-to-one relationship between Lecture and Course, where Lecture is the many in the relationship (make sure to add an appropriate related_name).
