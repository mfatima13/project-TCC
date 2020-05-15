from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action 

from .models import Team, Membership

from .serializers import MembershipSerializer, TeamSerializer


class TeamListCreate(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def listTeams(self):
        return self.objects.all()

    '''@action(detail=True, methods=['post'])
    def create(self, request):
        team = request.data
        print(team)
        return Response(status=status.HTTP_200_OK)'''

class TeamDeleteUpdate(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny]
