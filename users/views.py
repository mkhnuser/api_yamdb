from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer
from http import HTTPStatus


class BaseUserViewSet(APIView):
    def get(self, request, format=None):
        username = request.POST.get('username')

        if username:
            queryset = get_list_or_404(User.objects.all().filter(username=username))
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data, status=HTTPStatus.OK)

        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)


    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)



class SingleUserViewSet(APIView):
    def get(self, request, username:str=None, format=None):
        queryset = get_list_or_404(User.objects.all().filter(username=username))
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)

    def patch(self, request, username, format=None):
        pass
