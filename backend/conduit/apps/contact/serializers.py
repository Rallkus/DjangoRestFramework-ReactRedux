from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField(max_length=255)

    def validate(self, data):
        print "*************"
        print data

        email = data.get('email', None)
        subject = data.get('subject', None)
        message = data.get('message', None)
        print subject

        # As mentioned above, an email is required. Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'A valid email address is required'
            )

        # As mentioned above, a password is required. Raise an exception if a
        # password is not provided.
        if subject is None:
            raise serializers.ValidationError(
                'A subject is required'
            )

        if message is None:
            raise serializers.ValidationError(
                'A message is required and has to be at least 20 characters long'
            )



        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': email,
            'subject': subject,
            'message': message
        }