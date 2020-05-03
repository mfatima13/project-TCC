from django.contrib import admin
from .models import Team, Membership

class MembershipAdmin(admin.TabularInline):
    model = Team.members.through
    #model = Membership
    extra = 1

class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']
    empty_value_display = '-empty-'
    inlines = (MembershipAdmin,)

    

admin.site.register(Membership)
admin.site.register(Team, TeamAdmin)