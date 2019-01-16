from rest_framework import serializers

from conduit.apps.profiles.serializers import ProfileSerializer

from .models import PersonalTrainer


class PersonalTrainerSerializer(serializers.ModelSerializer):
    username = ProfileSerializer(read_only=True)
    bio = serializers.CharField(required=False)
    image = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    # Django REST Framework makes it possible to create a read-only field that
    # gets it's value by calling a function. In this case, the client expects
    # `created_at` to be called `createdAt` and `updated_at` to be `updatedAt`.
    # `serializers.SerializerMethodField` is a good way to avoid having the
    # requirements of the client leak into our API.


    class Meta:
        model = PersonalTrainer
        fields = (
            'slug',
            'username',
            'bio',
            'image',
        )

