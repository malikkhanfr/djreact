from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='')

    content = models.TextField()

    objects = models.Manager()
    def __str__(self):
        return self.title