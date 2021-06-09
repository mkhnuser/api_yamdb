from django.urls import include, path
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ReviewListAPIView,
    ReviewDetailAPIView,
    CommentListAPIView,
    CommentDetailAPIView
)

from . import views as title_views

router = routers.DefaultRouter()
router.register(r'genres', title_views.GenreViewSet)
router.register(r'titles', title_views.TitleViewSet)


urlpatterns = [
    path(
        'v1/categories/',
        CategoryViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='categories_list_create'
    ),
    path(
        'v1/categories/<str:slug>/',
        CategoryViewSet.as_view({'delete': 'destroy'}),
        name='categories_destroy'
    ),
    path(
        'v1/titles/<int:title_id>/reviews/',
        ReviewListAPIView.as_view(),
        name='reviews_list'
    ),
    path(
        'v1/titles/<int:title_id>/reviews/<int:review_id>/',
        ReviewDetailAPIView.as_view(),
        name='reviews_detail'
    ),
    path(
        'v1/titles/<int:title_id>/reviews/<int:review_id>/comments/',
        CommentListAPIView.as_view(),
        name='comments_list'
    ),
    path(
        ('v1/titles/<int:title_id>/reviews/'
         '<int:review_id>/comments/<int:comment_id>/'),
        CommentDetailAPIView.as_view(),
        name='comments_detail'
    ),
    path('v1/', include(router.urls)),
]
