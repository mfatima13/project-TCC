from django import forms

from .models import Team, Membership

class TeamForm(forms.Form):
    
    class Meta:
        model = Team
        fields = ('name', 'create_date', 'modify_date')
