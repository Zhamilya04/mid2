from django.contrib.auth.models import User
from django.db import models
from courses.models import Course

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(User, related_name="courses")

class FavoriteCourse(models.Model):
user = models.ForeignKey(User, on_delete=models.CASCADE)
course = models.ForeignKey(Course, on_delete=models.CASCADE)
class Meta:
    unique_together = ('user', 'course')