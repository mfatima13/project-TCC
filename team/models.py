from django.db import models
from account.models import CustomUser


class Team(models.Model):  # mudar nomeclaturas para project
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(
        CustomUser,
        # related_name='members',
        through='Membership',
        through_fields=('team', 'user'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="teams"
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="members"
    )
