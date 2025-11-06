from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subject_speciality = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
