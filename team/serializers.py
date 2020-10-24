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
    # user = CustomUserSerializer(many=True, read_only=True)
    # team = TeamSerializer(many=True, read_only=True, )
    """team = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name',
    )"""

    class Meta:
        model = Membership
        fields = [
            'id',
            'user',
            'team'
        ]
