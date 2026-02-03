from django.db import models

class Dataset(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='datasets/')
    summary = models.JSONField()

    def __str__(self):
        return f"Dataset uploaded at {self.uploaded_at}"
