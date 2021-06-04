from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views as title_views

router = routers.DefaultRouter()

"""
router.register(
    r'titles/<title_id:int>/reviews',
    title_views.ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/<title_id:int>/reviews/<review_id:int>/comments',
    title_views.CommentViewSet,
    basename='reviews'
)
router.register(
    r'categories',
    title_views.CategoryViewSet,
    basename='categories'
)
router.register(
    r'genres',
    title_views.GenreViewSet,
    basename='genres'
)
router.register(
    r'titles',
    title_views.TitleViewSet,
    basename='titles'
)
"""

router.register(r'categories', title_views.CategoryViewSet)
router.register(r'genres', title_views.GenreViewSet)
router.register(r'titles', title_views.TitleViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    #path('titles', title_views.TitleView.as_view()),
    path('', include(router.urls)),
    ]
