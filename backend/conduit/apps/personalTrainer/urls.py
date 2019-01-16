from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    PersonalTrainerAPIView
)

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^personalTrainers/?$', PersonalTrainerAPIView.as_view()),
]
