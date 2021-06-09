from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import EmailCodeVerificationView, AuthenticationView


urlpatterns = [
    path(
        'v1/auth/token/',
        csrf_exempt(AuthenticationView.as_view()),
        name='token-obtain'
    ),
    path(
        'v1/auth/email/',
        csrf_exempt(EmailCodeVerificationView.as_view()),
        name='email-verification'
    ),
    path(
        'v1/auth/token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    ),
]
