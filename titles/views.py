from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework import pagination, filters, mixins, authentication, generics
from django.shortcuts import get_object_or_404
from .models import Category, Genre, Title
from .serializers import CategotySerializer, GenreSerializer, TitleSerializer, TitleCreateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination 
    lookup_field = 'slug'     


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination 
    lookup_field = 'slug'  

class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):       
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['name',]
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination 
    #lookup_field = 'slug'    
    serializer_action_classes = {
            'list': TitleSerializer,
            'create': TitleCreateSerializer,
            'retrieve': TitleSerializer,
            #'update': MySerializer,
            #'partial_update': MySerializer,
            # etc.
        }

    def get_serializer_class(self):       
        try:
            #print(self.serializer_action_classes[self.action])
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return TitleSerializer


    

