from rest_framework import serializers

from .models import Team, Membership
from account.models import CustomUser
from account.serializers import CustomUserSerializer

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'create_date',
            'modify_date',
            'members'
        ]

class MembershipSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField(many=True, read_only=False)
    #team = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Membership
        fields = [
            'team',
            'user'
        ]
        