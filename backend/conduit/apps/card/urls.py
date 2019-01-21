from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    CardAPIView
)

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^cards/?$', CardAPIView.as_view()),
]
