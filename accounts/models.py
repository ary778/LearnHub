# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProgress(models.Model):
    # This class defines the choices for the resource_type field
    class ResourceType(models.TextChoices):
        YOUTUBE = 'YT', 'YouTube'
        BOOK = 'BK', 'Book'
        PROBLEM = 'CF_P', 'Codeforces Problem'
        BLOG = 'CF_B', 'Codeforces Blog'

    # This class defines the choices for the status field
    class Status(models.TextChoices):
        SAVED = 'SAVED', 'Saved for Later'
        COMPLETED = 'COMP', 'Completed'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    resource_type = models.CharField(max_length=5, choices=ResourceType.choices)
    resource_id = models.CharField(max_length=255)
    resource_title = models.CharField(max_length=255)
    resource_url = models.URLField()
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.SAVED)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'resource_type', 'resource_id')
        verbose_name_plural = "User Progress"

    def __str__(self):
        # The get_status_display() method is a standard Django feature.
        # It automatically gets the readable name from the 'choices' (e.g., 'Saved for Later').
        # This will work correctly after migrations.
        return f'{self.user.username} - {self.get_status_display()} - {self.resource_title}'