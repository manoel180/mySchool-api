from django.db import models

from mySchoolApp.models.course import Course


class Student(models.Model):
    name = models.CharField(unique=True, max_length=200, blank=False)
    email = models.EmailField(blank=False, unique=True)
    birthdate = models.DateField()
    course = models.ManyToManyField(Course)

    class Meta:
        db_table = 'students'
