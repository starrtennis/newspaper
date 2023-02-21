# articles/models.py
from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])