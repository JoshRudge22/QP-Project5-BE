from django.db import models
from django.contrib.auth.models import User

class Journey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journeys')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.user.username}"