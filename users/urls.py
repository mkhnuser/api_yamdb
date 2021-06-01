from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from django.urls import path, include
from . import views as user_views


router = routers.DefaultRouter()
router.register(
    r'users',
    user_views.UserViewSet,
    basename='users'
)


urlpatters = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    ),
]
