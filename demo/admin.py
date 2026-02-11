from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin  # Import it first
from django.forms import ModelForm
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple
from .forms import GroupedModelChoiceField

from .models import Sport, SportProfile, UserProfile, Analysis, Song

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
    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = ("permissions",)
    fields = ("name", "permissions")

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "permissions":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            # Avoid a major performance hit resolving permission names which
            # triggers a content_type load:
            kwargs["queryset"] = qs.select_related("content_type")
            return GroupedModelChoiceField(
                queryset=kwargs["queryset"],
                choices_groupby='content_type',
                widget=FilteredSelectMultiple(verbose_name="User permissions", is_stacked=False),
                required=False,
            )
        return super().formfield_for_manytomany(db_field, request=request, **kwargs)

class SongInline(admin.TabularInline):
    model = Song


class AnalysisAdmin(admin.ModelAdmin):
    inlines = [SongInline]


admin.site.register(Sport)
admin.site.register(SportProfile, ProfileAdmin)
admin.site.register(UserProfile)
admin.site.register(Permission)
admin.site.register(Analysis, AnalysisAdmin)
