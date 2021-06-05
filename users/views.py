from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.custom_permission import IsAdminUser
from users.models import User
from users.serializers import UserSerializer
from http import HTTPStatus


class BaseUserViewSet(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminUser, IsAuthenticated)

        username = request.POST.get('username')

        if username:
            user = get_object_or_404(User, username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=HTTPStatus.OK)

        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)


    def post(self, request, format=None):
        permission_classes = (IsAdminUser, IsAuthenticated)

        serializer = UserSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)



class SingleUserViewSet(APIView):
    def get(self, request, username:str=None, format=None):
        permission_classes = (IsAdminUser, IsAuthenticated)

        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTPStatus.OK)

    def patch(self, request, username, format=None):
        permission_classes = (IsAdminUser, IsAuthenticated)

        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def delete(self, request, username, format=None):
        permission_classes = (IsAdminUser, IsAuthenticated)

        user = get_object_or_404(User, username=username)
        user.delete()
        return Response(status=HTTPStatus.NO_CONTENT)


class MeUserViewSet(APIView):
    def get(self, request, format=None):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTPStatus.OK)

    def patch(self, request, username, format=None):
        user = get_object_or_404(User, username=request.user.username)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
