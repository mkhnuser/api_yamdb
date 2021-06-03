from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import EmailCodeVerification


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path(
        'email/', 
        csrf_exempt(EmailCodeVerification.as_view()), 
        name='code-verification'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    ),
]
