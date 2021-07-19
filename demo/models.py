from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    is_team_sport = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    sports = models.ManyToManyField(Sport)
