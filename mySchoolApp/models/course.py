from django.db import models

class Course(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        db_table = 'courses'
