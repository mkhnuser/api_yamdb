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
# router.register(r'categories', title_views.CategoryViewSet)
router.register(r'genres', title_views.GenreViewSet)
router.register(r'titles', title_views.TitleViewSet)


urlpatterns = [
    path(
        'categories/',
        CategoryViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='categories_list_create'
    ),
    path(
        'categories/<str:slug>/',
        CategoryViewSet.as_view({'delete': 'destroy'}),
        name='categories_destroy'
    ),
    path(
        'titles/<int:title_id>/reviews/',
        ReviewListAPIView.as_view(),
        name='reviews_list'
    ),
    path(
        'titles/<int:title_id>/reviews/<int:review_id>/',
        ReviewDetailAPIView.as_view(),
        name='reviews_detail'
    ),
    path(
        'titles/<int:title_id>/reviews/<int:review_id>/comments/',
        CommentListAPIView.as_view(),
        name='comments_list'
    ),
    path(
        ('titles/<int:title_id>/reviews/'
         '<int:review_id>/comments/<int:comment_id>/'),
        CommentDetailAPIView.as_view(),
        name='comments_detail'
    ),
    path('', include(router.urls)),
]
