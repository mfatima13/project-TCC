from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserVeiwSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def destroy(self, request, pk):
        print("meu delete ", pk)
        user = self.queryset.get(pk=pk)
        user.is_active = False
        user.save()
        print(user.is_active)

        return Response(
            {'message': 'o usuário foi desativado'}, 
            status=status.HTTP_204_NO_CONTENT
        )