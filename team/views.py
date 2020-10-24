from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend

from .models import Team, Membership

from .serializers import MembershipSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('-create_date', '-modify_date')
    serializer_class = TeamSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny
    ]
    filter_fields = ('members', )

    @action(detail=True, methods=['get'])
    def listTeams(self):
        return self.objects.all()

    @action(detail=True, methods=['post'])
    def createTeam(self, request):

        serializer = TeamSerializer(request.data)
        if serializer.is_valid():
            # Membership.objects.create(team=, user=)
            serializer.save()

            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def updateTeam(self, request):
        #      date = new_datetime
        #       print(date)
        '''TeamSerializer(data={
                request.data.name,
                request.data.create-date,
                date,
                request.data.members,
        })'''
        serializer = TeamSerializer(request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View responsavel pela relação muitos para muito da tabela members
class MembersViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny
    ]
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('team', 'user', )

    @action(methods=['get', ], detail=False)
    def teste(self, request):

        return Response(2+2, status=status.HTTP_200_OK)

    @action(methods=['get', ], detail=False)
    def teams(self, request):

        # get id user from query params
        user = request.query_params.get('user')
        # filter teams ids where user has relation
        members = self.queryset.filter(user=user).values()
        # filter teams by ids with pk__in
        teams = Team.objects.filter(pk__in=members.values_list('team_id'))

        teamsList = TeamSerializer(teams, many=True)

        return Response(teamsList.data, status=status.HTTP_200_OK)

    # @action(detail=True, methods=['post'], )
    def members_create(self, request, format=None):
        print("\nmembers create")
        serializer = MembershipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
