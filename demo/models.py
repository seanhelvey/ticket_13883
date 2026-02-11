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

class Analysis(models.Model):
    pass

class Song(models.Model):
    users = models.ManyToManyField("auth.User")
    analysis = models.ForeignKey("Analysis", on_delete=models.CASCADE, null=True)
