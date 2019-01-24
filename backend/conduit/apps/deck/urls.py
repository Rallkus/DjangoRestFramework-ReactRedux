from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    DeckAPIView
)

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^decks/?$', DeckAPIView.as_view()),
]
