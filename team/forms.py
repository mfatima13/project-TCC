from django import forms

from .models import Team


class TeamForm(forms.Form):

    class Meta:
        model = Team
        fields = ('name', 'create_date', 'modify_date')
