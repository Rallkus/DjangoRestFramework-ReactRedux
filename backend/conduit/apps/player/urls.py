from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    PlayerAPIView
)

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^players/?$', PlayerAPIView.as_view()),
]
