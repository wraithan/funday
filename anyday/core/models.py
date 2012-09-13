from django.db import models


class Funday(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    video = models.URLField()

    def __unicode__(self):
        return self.name
