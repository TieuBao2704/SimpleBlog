from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(default=datetime.now(), null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('theblog:detailpost', args=(str(self.id)))
        return reverse('theblog:homepage')