from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin  # Import it first
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .forms import GroupForm

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

# Unregister the default GroupAdmin (now it's loaded)
admin.site.unregister(Group)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    filter_horizontal = ('permissions',)

admin.site.register(Sport)
admin.site.register(SportProfile, ProfileAdmin)
admin.site.register(UserProfile)
