from django.db import models


class Funday(models.Model):
    # meta data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # details
    description = models.TextField()
    name = models.CharField(max_length=255)
    video = models.URLField()

    # filterables
    game_type = models.CharField(max_length=20,
                                 choices=(('individual', 'Individual'),
                                          ('team', 'Team'),
                                          ('ffa', 'Free For All')),
                                 default='individual')
    protoss = models.BooleanField(default=True)
    terran = models.BooleanField(default=True)
    zerg = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
