from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework import pagination, filters, mixins, authentication, generics
from django.shortcuts import get_object_or_404
from .models import Category, Genre, Title
from .serializers import CategotySerializer, GenreSerializer, TitleSerializer
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

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['name',]
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = pagination.PageNumberPagination 
    #lookup_field = 'slug'    


    

