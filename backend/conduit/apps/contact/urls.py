from django.conf.urls import url

from .views import (
    ContactAPIView
)

urlpatterns = [
    url(r'^contact/?$', ContactAPIView.as_view()),
]
