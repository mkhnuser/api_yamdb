from rest_framework import routers
from django.urls import path, include
from . import views as user_views


urlpatterns = [
    path('', user_views.BaseUserViewSet.as_view()),
    path('<str:username>/', user_views.SingleUserViewSet.as_view()),
]
