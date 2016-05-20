from django.db import models
from django.utils import timezone

class Mail(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    files = models.FileField(blank=True)
    email = models.EmailField()

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
