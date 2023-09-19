from api.models import Profile, StatusMessage
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo']


class StatusMessageSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = StatusMessage
        fields = '__all__'
