from django.shortcuts import render
from django.utils.datetime_safe import new_datetime
from rest_framework import viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action 

from account.models import CustomUser

from .models import Team, Membership

from .serializers import MembershipSerializer, TeamSerializer


class TeamListCreate(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('-create_date', '-modify_date')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def listTeams(self):
        return self.objects.all()

    @action(detail=True, methods=['post'])
    def createTeam(self, request):
        members = CustomUser.objects.filter(pk = request.data.members)
        teamName = request.data.name

        serializer = TeamSerializer(request.data)
        if serializer.is_valid():
            #Membership.objects.create(team=, user=)
            serializer.save()
            print(team)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDeleteUpdate(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.AllowAny]

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

class Members(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.AllowAny]

    def post(self, request, format=None):
        serializer = MembershipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
