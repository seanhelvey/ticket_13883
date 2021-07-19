from django.contrib import admin
from django.forms import ModelForm

from .models import Sport, Profile

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        team_sports = []
        single_sports = []
        for sport in Sport.objects.all():
            if sport.is_team_sport:
                team_sports.append((sport.name, sport.name))
            else:
                single_sports.append((sport.name, sport.name))
        self.fields['sports'].choices = [['Team Sports', team_sports], ['Single Sports', single_sports]]

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    filter_horizontal = ('sports',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Sport)
