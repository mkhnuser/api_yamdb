from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views as title_views

router = routers.DefaultRouter()
router.register(r'categories', title_views.CategoryViewSet)
router.register(r'genres', title_views.GenreViewSet)
router.register(r'titles', title_views.TitleViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router.urls)),
]
