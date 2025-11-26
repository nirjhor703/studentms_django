# videos/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    drive_file_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def direct_url(self):
        # Generates direct download URL from file_id
        return f"https://drive.google.com/uc?export=download&id={self.drive_file_id}"