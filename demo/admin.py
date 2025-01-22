from django.contrib import admin
from django.forms import ModelForm

from .models import Sport, SportProfile, UserProfile

class SportProfileForm(ModelForm):
    class Meta:
        model = SportProfile
        fields = ['sports']

    def __init__(self, *args, **kwargs):
        super(SportProfileForm, self).__init__(*args, **kwargs)

        team_sports = []
        single_sports = []
        for sport in Sport.objects.all():
            if sport.is_team_sport:
                team_sports.append((sport.id, sport.name))
            else:
                single_sports.append((sport.id, sport.name))
        self.fields['sports'].choices = [['Team Sports', team_sports], ['Single Sports', single_sports]]

class ProfileAdmin(admin.ModelAdmin):
    form = SportProfileForm
    filter_horizontal = ('sports',)

admin.site.register(Sport)
admin.site.register(SportProfile, ProfileAdmin)
admin.site.register(UserProfile)

