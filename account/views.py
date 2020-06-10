from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from .models import CustomUser

from .serializers import CustomUserSerializer


class UserlistCreate(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active = True)
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def listUsers(self):
        return self.objects.all()

    @action(detail=True, methods=['post'])
    def createUser(self, request):
        serializer = CustomUserSerializer(request.data)
        
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class UserUpdateDelete(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active = True)
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.AllowAny]

    @action(detail=True, methods=['delete'])
    def delete(self, pk, request):
        user = self.objects.get(pk=pk)
        user.is_active = False
        user.save()
        serializer = CustomUserSerializer(user)
        return Response(serializer, status=status.HTTP_200_OK)
'''
    @action(detail=True, methods=['put'])
    def update(self, request):
        serializer = CustomUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class MembersListCreate(viewsets.ModelViewSet):
    pass