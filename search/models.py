from django.conf import settings
from django.db import models

class Course(models.Model):
    topic = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

class Resource(models.Model):
    TYPE_CHOICES = [
        ('youtube', 'YouTube'),
        ('book', 'Book'),
        ('cf_problem', 'Codeforces Problem'),
        ('cf_blog', 'Codeforces Blog'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='resources')
    rtype = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=300)
    url = models.URLField()
    meta = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        type_map = dict(self.TYPE_CHOICES)
        rtype_display = type_map.get(self.rtype, self.rtype)
        return f"{rtype_display}: {self.title[:40]}"

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    percent = models.PositiveIntegerField(default=0)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} – {self.course} – {self.percent}%"
