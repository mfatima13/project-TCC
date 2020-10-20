from rest_framework import serializers

from .models import Team, Membership


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=True, )

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
    # user = serializers.StringRelatedField(many=True, read_only=False)
    # team = serializers.StringRelatedField(many=True, read_only=True, )

    class Meta:
        model = Membership
        fields = [
            'id',
            'team',
            'user',
        ]

    def update(self, validated_data):
        pass
