from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (filters, mixins,
                            pagination, permissions, viewsets)

from .filters import TitleFilter
from .models import Category, Genre, Title
from .permissions import CustomRolePermissions
from .serializers import (CategotySerializer, GenreSerializer,
                          TitleCreateSerializer, TitleSerializer)


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CustomRolePermissions]
    pagination_class = pagination.PageNumberPagination
    lookup_field = 'slug'


class GenreViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CustomRolePermissions]
    pagination_class = pagination.PageNumberPagination
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, CustomRolePermissions]
    pagination_class = pagination.PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', ]
    filterset_class = TitleFilter
    serializer_action_classes = {
        'list': TitleSerializer,
        'create': TitleCreateSerializer,
        'retrieve': TitleSerializer,
        'update': TitleCreateSerializer,
        'partial_update': TitleCreateSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return TitleSerializer
