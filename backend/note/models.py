import uuid
from django.db import models
from user.models import User
from django.utils.text import slugify


class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    is_trash = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    class Meta:
        ordering = ["created_at"]
