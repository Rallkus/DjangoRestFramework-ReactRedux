from django.core.mail import send_mail, BadHeaderError
from rest_framework import permissions, status, views, viewsets
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json


class ContactAPIView(views.APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        """
        return Response({
                    'status': 'true',
                    'message': 'Success! Thank you for your message'
                }, status=status.HTTP_200_OK)
        """
        data = request.data
        print '**********************************'
        print data
        print '**********************************'
        body = data.get('body', None)
        print body
        result = json.loads(body)
        print result
        email = result.get('email', None)
        print email
        print 'email'
        print '**********************************'
        subject = result.get('subject', None)
        print subject
        print '**********************************'
        message = result.get('message', None)
        print message
        print '**********************************'
        
        """
        return Response({
                    'status': 'true',
                    'message': 'Success! Thank you for your message'
                }, status=status.HTTP_200_OK)
        """
        
        if email is None:
            return Response({
                    'status': 'false',
                    'message': "'email' field is missing"
                }, status=status.HTTP_400_BAD_REQUEST)
        elif subject is None:
            return Response({
                    'status': 'false',
                    'message': "'subject' field is missing"
                }, status=status.HTTP_400_BAD_REQUEST)
        elif message is None:
            return Response({
                    'status': 'false',
                    'message': "'message' field is missing"
                }, status=status.HTTP_400_BAD_REQUEST)
            
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
