from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    file = models.FileField(upload_to='datasets/')  # Adjust upload path as needed
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # If you associate datasets with users
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
