from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple
from functools import partial
from itertools import groupby
from operator import attrgetter
from django.forms.models import ModelChoiceIterator

class GroupedModelChoiceIterator(ModelChoiceIterator):
    def __init__(self, field, groupby):
        self.groupby = groupby
        super().__init__(field)

    def __iter__(self):
        queryset = self.queryset
        if not queryset._prefetch_related_lookups:
            queryset = queryset.iterator()
        for group, objs in groupby(queryset, self.groupby):
            yield (group, [self.choice(obj) for obj in objs])

class GroupedModelChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, choices_groupby, **kwargs):
        if isinstance(choices_groupby, str):
            choices_groupby = attrgetter(choices_groupby)
        elif not callable(choices_groupby):
            raise TypeError('choices_groupby must be str or callable')
        self.iterator = partial(GroupedModelChoiceIterator, groupby=choices_groupby)
        super().__init__(*args, **kwargs)

class GroupForm(forms.ModelForm):
    permissions = GroupedModelChoiceField(
        queryset=Permission.objects.all().select_related("content_type"),
        choices_groupby='content_type',
        widget=FilteredSelectMultiple("Permissions", False),
        required=False,
    )
    
    class Meta:
        model = Group
        fields = ['name', 'permissions']
