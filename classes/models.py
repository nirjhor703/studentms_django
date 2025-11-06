from django.db import models

# classes/models.py
from django.db import models
from teachers.models import Teacher
from subjects.models import Subject

class ClassModel(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

