from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Player
from .renderers import PlayerJSONRenderer
from .serializers import PlayerSerializer

class PlayerAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    renderer_classes = (PlayerJSONRenderer,)
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )

        return self.get_paginated_response(serializer.data)


