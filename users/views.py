from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import HasAdminRole
from users.models import User
from users.serializers import UserSerializer
from http import HTTPStatus


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, HasAdminRole,)

    def get_object(self):
        username = self.kwargs.get('pk')
        return get_object_or_404(User, username=username)


class MeUserViewSet(APIView):
    def get(self, request, format=None):
        user = get_object_or_404(User, username=self.request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTPStatus.OK)

    def patch(self, request, format=None):
        user = get_object_or_404(User, username=self.request.user.username)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.error, status=HTTPStatus.BAD_REQUEST)
