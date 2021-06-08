from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (filters, mixins,
                            pagination, permissions, viewsets)

from .filters import TitleFilter
from .models import Category, Genre, Title, Review, Comment
from .permissions import CustomRolePermissions, IsOwnerOrReadOnly
from .serializers import (CategotySerializer, GenreSerializer,
                          TitleCreateSerializer, TitleSerializer,
                          ReviewSerializer, CommentSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from apps.account.permissions import IsAuthorOrReadOnlyPermission


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategotySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        CustomRolePermissions
    ]
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


class ReviewListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        return self.queryset.filter(title_id=self.kwargs['title_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthorOrReadOnlyPermission]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewSerializer

    def get_object(self):
        obj = get_object_or_404(
            Review,
            title_id=self.kwargs['title_id'],
            id=self.kwargs['review_id']
        )
        self.check_object_permissions(self.request, obj)
        return obj


class CommentListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return self.queryset.filter(review_id=self.kwargs['review_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthorOrReadOnlyPermission]
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def get_object(self):
        obj = get_object_or_404(
            Comment,
            review__title_id=self.kwargs['title_id'],
            review_id=self.kwargs['review_id'],
            id=self.kwargs['comment_id']
        )
        self.check_object_permissions(self.request, obj)
        return obj
