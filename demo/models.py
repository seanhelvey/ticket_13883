from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    is_team_sport = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SportProfile(models.Model):
    sports = models.ManyToManyField(Sport)

class UserProfile(models.Model):
    user = models.ForeignKey("auth.User", models.CASCADE, to_field="username")

    def __str__(self):
        return self.user.username
