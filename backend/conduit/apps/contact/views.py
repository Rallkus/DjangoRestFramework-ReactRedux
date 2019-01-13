from django.core.mail import send_mail, BadHeaderError
from rest_framework import permissions, status, views, viewsets
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
from .serializers import (
    ContactSerializer
)


class ContactAPIView(views.APIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer
    def post(self, request):      

        form = request.data
        print form
        body = form.get('body', None)
        result = json.loads(body)
        email = result.get('email', None)
        subject = result.get('subject', None)
        message = result.get('message', None)
        serializer = self.serializer_class(data=result)
        serializer.is_valid(raise_exception=True)
        print "IMPORTANT"
        print 

        if serializer.is_valid(raise_exception=True):
            
            try:
                send_mail(subject, message, 'serhuegi@gmail.com', [email])
            except BadHeaderError:
                return Response({
                        'status': 'false',
                        'message': 'BadHeaderError for your message'
                    }, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            return Response({
                        'status': 'true',
                        'message': 'Success! Thank you for your message'
                    }, status=status.HTTP_200_OK)
        return Response({
                        'status': 'false',
                        'message': 'Something is wrong with your form, check it out!'
                    }, status=status.HTTP_503_SERVICE_UNAVAILABLE)