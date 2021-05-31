from rest_framework import routers
from django.urls import path, include
from . import views as title_views


router = routers.DefaultRouter()
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


urlpatterns = [
    path('', include(router.urls)),
]
