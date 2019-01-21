from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card
from .renderers import CardJSONRenderer
from .serializers import CardSerializer

class CardAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    renderer_classes = (CardJSONRenderer,)
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )

        return self.get_paginated_response(serializer.data)


