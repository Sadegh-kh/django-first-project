from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISH)


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = ("DR", "Draft")
        PUBLISH = ("PB", "Publish")
        REJECT = ("RJ", "Reject")

    # relation
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posted")
    # data fields
    title = models.CharField(max_length=250)
    description = models.TextField()

    slug = models.SlugField(max_length=250)

    # date fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    # choice field
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=["-publish"])
        ]

    def __str__(self):
        return self.title
